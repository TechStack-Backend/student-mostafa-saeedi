from django.urls import path
from . import views

urlpatterns = [
    path('developers/', views.developers_list, name='developers_list'),
    path('projects/', views.projects_list, name='projects_list'),
    path('add-developer/', views.add_developer, name='add_developer'),
    path('add-project/', views.add_project, name='add_project'),
]
