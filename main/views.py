from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from .models import TodoTask
# Create your views here.
class UserLogin(LoginView):
    template_name = 'main/login.html'
    fields = '__all__'
    redirect_authenticated_user = 'True'

    def get_success_url(self):
        return reverse_lazy('Task')

class TodoList(ListView):
    model = TodoTask
    context_object_name = 'TodoList'

class TodoListDetail(DetailView):
    model = TodoTask
    context_object_name = 'task'
    template_name = 'main/detail.html'

class CreateTask(CreateView):
    model = TodoTask
    fields = '__all__'
    template_name = 'main/task_form.html'
    success_url = reverse_lazy('Task')

class UpdateTask(UpdateView):
    model = TodoTask
    fields = '__all__'
    template_name = 'main/task_form.html'
    success_url = reverse_lazy('Task')

class DeleteTask(DeleteView):
    model = TodoTask
    context_object_name = 'TodoList'
    template_name = 'main/delete_task.html'
    success_url = reverse_lazy('Task')