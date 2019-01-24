from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Department(models.Model):
    dept_id = models.CharField(max_length = 20, primary_key = True)
    dept_name = models.CharField(max_length = 30)

    def __str__(self):
        return ''+self.dept_name

class TeacherProfile(models.Model):
    teacher_id = models.CharField(max_length = 10, primary_key = True)
    teacher_name = models.CharField(max_length = 40)
    dept_id = models.ForeignKey(Department, db_column = 'dept_id', on_delete = models.CASCADE)
    teacher_shortCode = models.CharField(max_length = 5)
    teacher_designation = models.CharField(max_length = 20)
    teachers_university = models.CharField(max_length = 20)

    def __str__(self):
        return ''+self.teacher_shortCode

class ExaminationSystem(models.Model):
    EXAM_CATEGORY = (
        ('UG', 'Undergraduate'),
        ('PG', 'Postgraduate'),
        ('PD', 'Doctorate'),
        ('EX', 'Executive Program'),
    )

    YEAR_SEMESTER = (
        ('1-1', '1st Year - 1st Semester'),
        ('1-2', '1st Year - 2nd Semester'),
        ('2-1', '2nd Year - 1st Semester'),
        ('2-2', '2nd Year - 2nd Semester'),
        ('3-1', '3rd Year - 1st Semester'),
        ('3-2', '3rd Year - 2nd Semester'),
        ('4-1', '4th Year - 1st Semester'),
        ('4-2', '4th Year - 2nd Semester'),
    )

    examination_id = models.CharField(max_length = 5, primary_key = True)
    examination_level = models.CharField(max_length = 2, choices = EXAM_CATEGORY)
    semester_selection = models.CharField(max_length = 3, choices = YEAR_SEMESTER)
    examination_year = models.CharField(max_length = 4)

    def __str__(self):
        return ''+self.examination_level
class SubjectCreation(models.Model):
    CREDIT = (
        ('0.75', '0.75 Credit'),
        ('1.00', '1.00 Credit'),
        ('1.50', '1.50 Credit'),
        ('2.00', '2.00 Credit'),
        ('3.00', '3.00 Credit'),
        ('4.00', '4.00 Credit'),
    )
    sibject_id = models.CharField(max_length = 5, primary_key = True)
    select_department = models.ForeignKey(Department, db_column = 'dept_id', on_delete = models.CASCADE)
    select_semester_year = models.ForeignKey(ExaminationSystem, db_column = 'semester_selection', on_delete = models.CASCADE)
    course_code = models.IntegerField()
    course_name = models.CharField(max_length = 30)
    course_credit = models.CharField(max_length = 1, choices = CREDIT)

    def __str__(self):
        return ''+self.course_code


#END OF BASIC MODELS

class ExamProposal(models.Model):
    exam_proposal_id = models.CharField(max_length = 5, primary_key = True)
    exam_of_the_department = models.ManyToManyField(Department)
    proposed_examination_to_take = models.ManyToManyField(ExaminationSystem)
    commitee_cheaf = models.ForeignKey(TeacherProfile, related_name="ChiefMember", on_delete=models.CASCADE, default = None)
    committee_member_one = models.ForeignKey(TeacherProfile, related_name="FirstMember", on_delete=models.CASCADE, default = None)
    committee_member_two = models.ForeignKey(TeacherProfile, related_name="SecoundMember", on_delete=models.CASCADE, default = None)
    
    def __str__(self):
        return ''+self.exam_proposal_id

class TheoryExamRoutineGenarator(models.Model):
    theory_exam_id = models.CharField(max_length = 5, primary_key = True)
    theory_exam_date_select = models.DateField()
    theory_exam_course_code_select = models.ForeignKey(SubjectCreation, db_column = 'course_code', related_name="theoryExamCode", on_delete=models.CASCADE)
    theory_exam_course_name_select = models.ForeignKey(SubjectCreation, db_column = 'course_name', related_name="theoryExamName", on_delete=models.CASCADE)
    theory_exam_course_credit_select = models.ForeignKey(SubjectCreation, db_column = 'course_credit', related_name="theoryExamCredit", on_delete=models.CASCADE)
    theory_exam_start_time_select = models.TimeField()
    theory_exam_end_time_select = models.TimeField()

    def __str__(self):
        return ''+self.theory_exam_id

class TheoryExamTabulatorGenarator(models.Model):
    theory_exam_tabulator_list_id = models.CharField(max_length = 5, primary_key = True)
    select_exam = models.ManyToManyField(TheoryExamRoutineGenarator)
    select_first_examiner = models.ForeignKey(TeacherProfile, related_name="FirstExaminerTheory", on_delete=models.CASCADE, default = None)
    select_secound_examiner = models.ForeignKey(TeacherProfile, related_name="SecoundExaminerTheory", on_delete=models.CASCADE, default = None)
    select_third_examiner = models.ForeignKey(TeacherProfile, related_name="ThirdExaminerTheory", on_delete=models.CASCADE, default = None)

    def __str__(self):
        return ''+self.theory_exam_tabulator_list_id

class LabExamRoutineGenarator(models.Model):
    lab_exam_id = models.CharField(max_length = 5, primary_key = True)
    lab_exam_date_select = models.DateField()
    lab_exam_course_code_select = models.ForeignKey(SubjectCreation, db_column = 'course_code', related_name="labExamCode", on_delete=models.CASCADE)
    lab_exam_course_name_select = models.ForeignKey(SubjectCreation, db_column = 'course_name', related_name="labExamName", on_delete=models.CASCADE)
    lab_exam_course_credit_select = models.ForeignKey(SubjectCreation, db_column = 'course_credit', related_name="labExamCredit", on_delete=models.CASCADE)
    lab_exam_start_time_select = models.TimeField()
    lab_exam_end_time_select = models.TimeField()

    def __str__(self):
        return ''+self.lab_exam_id


class LabExamTabulatorGenarator(models.Model):
    lab_exam_tabulator_list_id = models.CharField(max_length = 5, primary_key = True)
    select_exam = models.ManyToManyField(TheoryExamRoutineGenarator)
    select_first_examiner = models.ForeignKey(TeacherProfile, related_name="FirstExaminerLab", on_delete=models.CASCADE, default = None)
    select_secound_examiner = models.ForeignKey(TeacherProfile, related_name="SecoundExaminerLab", on_delete=models.CASCADE, default = None)
    select_third_examiner = models.ForeignKey(TeacherProfile, related_name="ThirdExaminerLab", on_delete=models.CASCADE, default = None)

    def __str__(self):
        return ''+self.lab_exam_tabulator_list_id

class VivaVoceExamRoutineGenarator(models.Model):
    viva_voce_id = models.CharField(max_length = 5, primary_key = True)
    viva_voce_date_select = models.DateField()
    viva_voce_course_code_select = models.ForeignKey(SubjectCreation, db_column = 'course_code', related_name="VivaVoceExamCode", on_delete=models.CASCADE)
    viva_voce_course_name_select = models.ForeignKey(SubjectCreation, db_column = 'course_name', related_name="VivaVoceExamName", on_delete=models.CASCADE)
    viva_voce_course_credit_select = models.ForeignKey(SubjectCreation, db_column = 'course_credit', related_name="VivaVoceExamCredit", on_delete=models.CASCADE)
    viva_voce_start_time_select = models.TimeField()
    viva_voce_end_time_select = models.TimeField()

    def __str__(self):
        return ''+self.viva_voce_id


class VivaVoceExamTabulatorGenarator(models.Model):
    viva_voce_tabulator_list_id = models.CharField(max_length = 5, primary_key = True)
    select_exam = models.ManyToManyField(TheoryExamRoutineGenarator)
    select_first_examiner = models.ForeignKey(TeacherProfile, related_name="FirstExaminerVivaVoce", on_delete=models.CASCADE, default = None)
    select_secound_examiner = models.ForeignKey(TeacherProfile, related_name="SecoundExaminerVivaVoce", on_delete=models.CASCADE, default = None)
    select_third_examiner = models.ForeignKey(TeacherProfile, related_name="ThirdExaminerVivaVoce", on_delete=models.CASCADE, default = None)

    def __str__(self):
        return ''+self.viva_voce_tabulator_list_id

class GenarateBillOfTheExaminer(models.Model):
    bill_id = models.CharField(max_length = 5, primary_key = True)
    examiner_name = models.ForeignKey(TeacherProfile, db_column = 'teacher_name', on_delete = models.CASCADE)
    examination_year_of_the_exam = models.ForeignKey(ExaminationSystem, db_column = 'examination_year', related_name="ExaminationYearBG", on_delete = models.CASCADE)
    examination_semester = models.ForeignKey(ExaminationSystem, db_column = 'semester_selection', related_name="ExaminationSemesterBG", on_delete = models.CASCADE)
    examination_grade = models.ForeignKey(ExaminationSystem, db_column = 'examination_level', related_name="ExaminationGradeBG", on_delete = models.CASCADE)

    #Working outline
    def __str__(self):
        return ''+self.bill_id

class DoneDutyTasksGenarator(models.Model):
    task_id = models.CharField(max_length = 5, primary_key = True)
    examiner_name = models.ForeignKey(TeacherProfile, db_column = 'teacher_name', on_delete = models.CASCADE)
    examination_year_of_the_exam = models.ForeignKey(ExaminationSystem, db_column = 'examination_year', related_name="ExaminationYearTG", on_delete = models.CASCADE)
    examination_semester = models.ForeignKey(ExaminationSystem, db_column = 'semester_selection', related_name="ExaminationSemesterTG", on_delete = models.CASCADE)
    examination_grade = models.ForeignKey(ExaminationSystem, db_column = 'examination_level', related_name="ExaminationGradeTG", on_delete = models.CASCADE)


    def __str__(self):
        return ''+self.task_id
