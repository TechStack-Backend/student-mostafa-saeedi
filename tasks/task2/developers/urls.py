from django.urls import path
from . import views

urlpatterns = [
    path('', views.developer_list, name='developer_list'),
    path('<str:username>/', views.developer_cv, name='developer_cv'),
]