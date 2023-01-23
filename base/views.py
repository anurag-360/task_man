from .models import Task
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm

# Create your views here.

# @login_required(login_url='login')
class TaskList(LoginRequiredMixin,ListView):
    model = Task
    context_object_name = 'all_tasks'
    # print(context_object_name.complete)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_tasks'] = context['all_tasks'].filter(user = self.request.user)
        # context['all_tasks'] = context['all_tasks'].ordering
        return context

    # def get_queryset(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['all_tasks'] = super(TaskList, self).get_queryset(**kwargs)
    #     context['all_tasks'] = context.order_by("deadline")
    #     return context


class TaskCreate(LoginRequiredMixin,CreateView):
    model = Task
    fields = ['task', 'complete', 'deadline']
    success_url = reverse_lazy('tasks')


    def form_valid(self,form):
        form.instance.user = self.request.user
        return super(TaskCreate,self).form_valid(form)

class TaskUpdate(LoginRequiredMixin,UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class TaskDelete(LoginRequiredMixin,DeleteView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
         
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('/task-list/')
        else:
            messages.info(request, 'Username OR Password is in correct')


    context= {}

    return render(request, "base/login.html", context)

def logOutUser(request):
    logout(request)
    return redirect("/login")

def deadlineSort(request):
    html = "<html><body>It is now %s.</body></html"
    return HttpResponse(html)

def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST' :
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        pass

    context = {'form':form}
    return render(request, "base/register.html", context)

