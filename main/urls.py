from django.urls import path
from .views import TodoList,TodoListDetail,CreateTask,UpdateTask,DeleteTask,UserLogin

urlpatterns = [
    path ('',UserLogin.as_view(), name='login'),
    path ('task/',TodoList.as_view(),name='Task'),
    path ('detail/<int:pk>/',TodoListDetail.as_view(),name='detail'),
    path ('createTask/',CreateTask.as_view(),name='createTask'),
    path ('updateTask/<int:pk>',UpdateTask.as_view(),name='updateTask'),
    path ('deleteTask/<int:pk>',DeleteTask.as_view(),name='deleteTask'),
]