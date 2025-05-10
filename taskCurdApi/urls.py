from django.urls import path
from . import views


urlpatterns = [
    # List all tasks and create new task
    path('tasks/', views.TaskView.as_view(), name='task-list-create'),
    
    # Get, update, and delete specific task
    path('tasks/<int:pk>/', views.TaskView.as_view(), name='task-detail'),
]
