from django.urls import path
from . import views

urlpatterns = [
    path('', views.quiz_home, name='quiz_home'),
    path('start/<int:topic_id>/', views.quiz_start, name='quiz_start'),
    path('take/<int:topic_id>/', views.take_quiz, name='take_quiz'),
]
