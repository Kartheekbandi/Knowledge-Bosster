from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.questions,name='questions'),
   path('mat', views.matquestions,name='matquestions'),
   path('gk', views.gkquestions,name='gkquestions'),
]