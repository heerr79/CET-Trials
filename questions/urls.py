from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('signup/', views.signup, name='signup'),
    path('subjects/', views.subjects, name='subjects'),
    path('syllabus/', views.syllabus, name='syllabus'),
    path('about/', views.about, name='about'),
    path('instruction1/', views.instruction1, name='instruction1'),
    path('instruction2/', views.instruction2, name='instruction2'),
    path('pcm/', views.pcm, name='pcm'),
    path('pcb/', views.pcb, name='pcb'),
    path('pcmp1/', views.pcmp1, name='pcmp1'),
    path('pcmc1/', views.pcmc1, name='pcmc1'),
    path('pcmm1/', views.pcmm1, name='pcmm1'),
    path('result/', views.result, name='result'),
    path('result1/', views.result1, name='result1'),
    path('result2/', views.result2, name='result2'),
    path('pcbp1/', views.pcbp1, name='pcbp1'),
    path('resultp1/', views.resultp1, name='resultp1'),
    path('pcbc1/', views.pcbc1, name='pcbc1'),
    path('resultc1/', views.resultc1, name='resultc1'),
    path('pcbb1/', views.pcbb1, name='pcbb1'),
    path('resultb1/', views.resultb1, name='resultb1'),
    # AI Exam Generation URLs
    path('generate-ai-exam/', views.generate_ai_exam, name='generate_ai_exam'),
    path('start-practice/', views.start_practice, name='start_practice'),
    path('ai-exam/<int:exam_id>/', views.take_ai_exam, name='take_ai_exam'),
    path('practice-session/<int:session_id>/', views.practice_session, name='practice_session'),
]
