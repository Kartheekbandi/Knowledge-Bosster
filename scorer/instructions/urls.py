from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.instructions,name='instructions'),
    path('mat', views.instructionsmat,name='instructionsmat'),
    path('gk', views.instructionsgk,name='instructionsgk'),
]