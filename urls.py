from django.urls import path
from django.conf.urls import include
from quiz import views

app_name = 'quiz'
urlpatterns = [
    path('', views.indexView.as_view()),
]