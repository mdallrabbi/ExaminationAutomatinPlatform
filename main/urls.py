from .import views
from .views import *

from django.urls import path

urlpatterns = [
	
	path('adddepartment/',CreateDepartmentQuery.as_view(), name = 'add_department'),
	path('addteacher/',CreateTeacherProfileQuery.as_view(), name = 'add_teacher'),
	path('addexaminationsystem/',CreateExaminationSystemQuery.as_view(), name = 'add_examination'),
	path('addsubject/',CreateSubjectCreationQuery.as_view(), name = 'add_subject'),
	path('createexamproposal/',CreateExamProposalQuery.as_view(), name = 'create_exam'),
	path('theoryexamroutine/',CreateTheoryExamRoutineGenaratorQuery.as_view(), name = 'theory_exam_routine'),
	path('theoryexamtabulator/',CreateTheoryExamTabulatorQuery.as_view(), name = 'theory_exam_tabulator'),
	path('labexamroutine/',CreateLabExamRoutineGenaratorQuery.as_view(), name = 'lab_exam_routine'),
	path('labexamtabulator/',CreateLabExamRoutineTabulatorQuery.as_view(), name = 'lab_exam_tabulator'),
	path('vivavoceroutine/',CreateVivaVoceRoutineGenaratorQuery.as_view(), name = 'viva_voce_routine'),
	path('vivavocetabulator/',CreateVivaVoceTabulatorQuery.as_view(), name = 'viva_voce_tabulator'),
	path('genaratebill/',CreateGeanarateBillOfTheExaminerQuery.as_view(), name = 'genarate_bill_of_theexaminer'),
	path('donedutylist/',CreateDoneDutyTaskGenaratorQuery.as_view(), name = 'done_duty_task'),

]