from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView
from django.urls import reverse_lazy
from .models import TodoTask
# Create your views here.
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