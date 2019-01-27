from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import *
# Create your views here.

class CreateDepartmentQuery(CreateView):
    model = Department
    fields = "__all__"
    template_name = "queryrequests/departmentquery.html"

class CreateTeacherProfileQuery(CreateView):
    model = TeacherProfile
    fields = "__all__"
    template_name = "queryrequests/teacherquery.html"
    
class CreateExaminationSystemQuery(CreateView):
    model = ExaminationSystem
    fields = "__all__"
    template_name = "queryrequests/createexamquery.html"

class CreateSubjectCreationQuery(CreateView):
    model = SubjectCreation
    fields = "__all__"
    template_name = "queryrequests/createsubjectquery.html"

class CreateExamProposalQuery(CreateView):
    model = ExamProposal
    fields = "__all__"
    template_name = "queryrequests/examproposalquery.html"

class CreateTheoryExamRoutineGenaratorQuery(CreateView):
    model = TheoryExamRoutineGenarator
    fields = "__all__"
    template_name = "queryrequests/theoryexamroutinequery.html"

class CreateTheoryExamTabulatorQuery(CreateView):
    model = TheoryExamTabulatorGenarator
    fields = "__all__"
    template_name = "queryrequests/theoryexamtabulatorquery.html"

class CreateLabExamRoutineGenaratorQuery(CreateView):
    model = LabExamRoutineGenarator
    fields = "__all__"
    template_name = "queryrequests/labexamroutinequery.html"

class CreateLabExamRoutineTabulatorQuery(CreateView):
    model = LabExamTabulatorGenarator
    fields = "__all__"
    template_name = "queryrequests/labexamtabulatorquery.html"

class CreateVivaVoceRoutineGenaratorQuery(CreateView):
    model = VivaVoceExamRoutineGenarator
    fields = "__all__"
    template_name = "queryrequests/vivavoceroutinequery.html"

class CreateVivaVoceTabulatorQuery(CreateView):
    model = VivaVoceExamTabulatorGenarator
    fields = "__all__"
    template_name = "queryrequests/vivavocetabulatorquery.html"

class CreateGeanarateBillOfTheExaminerQuery(CreateView):
    model = GenarateBillOfTheExaminer
    fields = "__all__"
    template_name = "queryrequests/genaratebillquery.html"

class CreateDoneDutyTaskGenaratorQuery(CreateView):
    model = DoneDutyTasksGenarator
    fields = "__all__"
    template_name = "queryrequests/donedutytaskquery.html"