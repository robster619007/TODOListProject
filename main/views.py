from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import TodoTask
# Create your views here.

# Login
class UserLogin(LoginView):
    template_name = 'main/login.html'
    fields = '__all__'
    redirect_authenticated_user = 'True'

    def get_success_url(self):
        return reverse_lazy('Task')
# Show Todo List
class TodoList(LoginRequiredMixin,ListView):
    model = TodoTask
    context_object_name = 'TodoList'
    # function to only show the todo list for the user's account
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['TodoList'] = context['TodoList'].filter(user = self.request.user)
        return context

# Show the details of the task in Todo List
class TodoListDetail(LoginRequiredMixin,DetailView):
    model = TodoTask
    context_object_name = 'task'
    template_name = 'main/detail.html'

# Create a task for the TodoList
class CreateTask(LoginRequiredMixin,CreateView):
    model = TodoTask
    fields = '__all__'
    template_name = 'main/task_form.html'
    success_url = reverse_lazy('Task')
    # Function to add tasks by user logged in
    # the task gets added in the user account logged in during that instance
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super(CreateTask,self).form_valid(form)

# Update the task in the todo list
class UpdateTask(LoginRequiredMixin,UpdateView):
    model = TodoTask
    fields = '__all__'
    template_name = 'main/task_form.html'
    success_url = reverse_lazy('Task')

# Delete the task in the todo list
class DeleteTask(LoginRequiredMixin,DeleteView):
    model = TodoTask
    context_object_name = 'TodoList'
    template_name = 'main/delete_task.html'
    success_url = reverse_lazy('Task')