from django.contrib import admin
from .models import *

# Register your models here.

main_models = [
    Department,
    TeacherProfile,
    ExaminationSystem,
    SubjectCreation,
    ExamProposal,
    TheoryExamRoutineGenarator,
    TheoryExamTabulatorGenarator,
    LabExamRoutineGenarator,
    LabExamTabulatorGenarator,
    VivaVoceExamRoutineGenarator,
    VivaVoceExamTabulatorGenarator,
    GenarateBillOfTheExaminer,
    DoneDutyTasksGenarator,


]

admin.site.register(main_models)

