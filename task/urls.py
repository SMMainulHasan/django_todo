from django.urls import path

from .views import (add_task, complete_task, completed_task, delete_task,
                    edit_task, show_tasks)

urlpatterns = [
    path('', show_tasks, name='show_tasks'),
    path('add_task', add_task, name='add_task'),
    path('delete/<int:id>', delete_task, name='delete_task'),
    path('edit/<int:id>', edit_task, name='edit_task'),
    path('complete/<int:id>', complete_task, name='complete_task'),
    path('completed_task/', completed_task, name='completed_task'),
]
