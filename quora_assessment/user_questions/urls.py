from django.urls import path
from . import views
from . import api_views

urlpatterns = [
    path('', views.question_list, name='home'),
    path('question/<int:id>/', views.question_detail, name='question_detail'),
    path('question/new/', views.new_question, name='new_question'),
    path('answer/<int:answer_id>/like/', views.like_answer, name='like_answer'),
    path('register/', views.register, name='register'),

    # API endpoints
    path('api/questions/', api_views.QuestionListCreateAPIView.as_view(), name='api_questions'),
    path('api/answers/', api_views.AnswerListCreateAPIView.as_view(), name='api_answers'),
    path('api/likes/', api_views.LikeCreateAPIView.as_view(), name='api_likes'),
]