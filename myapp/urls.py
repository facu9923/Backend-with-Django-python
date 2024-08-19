from django.urls import path

from . import views

urlpatterns = [
    path('', views.hello),
    path('about/', views.about),
    path('projects/', views.projects),
    path('tasks/', views.tasks),
    path('create_tasks/', views.create_tasks),
    path('create_project/', views.create_project)
]