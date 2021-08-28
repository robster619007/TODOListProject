from django.urls import path
from .views import TodoList,TodoListDetail,CreateTask,UpdateTask

urlpatterns = [
    path ('',TodoList.as_view(),name='Task'),
    path ('detail/<int:pk>/',TodoListDetail.as_view(),name='detail'),
    path ('createTask/',CreateTask.as_view(),name='createTask'),
    path ('updateTask/<int:pk>',UpdateTask.as_view(),name='updateTask'),
]