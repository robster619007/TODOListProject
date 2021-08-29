from django.urls import path
from .views import TodoList,TodoListDetail,CreateTask,UpdateTask,DeleteTask,UserLogin,SignUp
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path ('',UserLogin.as_view(), name='login'),
    path ('logout/',LogoutView.as_view(next_page='login'), name='logout'),
    path ('signup/',SignUp.as_view(), name='signup'),
    path ('task/',TodoList.as_view(),name='Task'),
    path ('detail/<int:pk>/',TodoListDetail.as_view(),name='detail'),
    path ('createTask/',CreateTask.as_view(),name='createTask'),
    path ('updateTask/<int:pk>',UpdateTask.as_view(),name='updateTask'),
    path ('deleteTask/<int:pk>',DeleteTask.as_view(),name='deleteTask'),
]