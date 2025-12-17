from django.shortcuts import render,redirect
from django.contrib.auth import logout, login
from .models import Project, Task, Comment
from django.contrib.auth.models import User
from .forms import RegisterForm, TaskForm, ProjectForm, CommentForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
import random

def home(request):

    projects = Project.objects.all()
    tasks = Task.objects.all()
    completed_tasks_count = tasks.filter(status='done').count()

    return render(request, "MAIN/home.html", {
        "projects": projects,
        "tasks": tasks,
        "completed_tasks_count": completed_tasks_count,
    })


@login_required
def task_detail_with_comments(request, pk):
    task = get_object_or_404(Task, pk=pk)

    show_comments = request.GET.get("comments") == "1"

    comments = task.comments.order_by('created_at') if show_comments else []

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.task = task
            comment.save()

            return redirect(f"{request.path}?comments=1")
    else:
        form = CommentForm()

    return render(request, "CRUD/task_detail.html", {
        'task': task,
        'comments': comments,
        'form': form,
        'show_comments': show_comments,
    })

def project(request):
    
    return render(request, "MAIN/project.html")



def logout_view(request):
    logout(request)
    return redirect('home')

def register(request):
    error = ''
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            if User.objects.filter(username=username).exists():
                error = 'USERNAME IS ALREADY EXISTED'

            else:
                user = form.save()
                
                group = form.cleaned_data['group']
                user.groups.add(group)
                
                login(request, user)
                return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'OTHER/register.html', {'form': form, 'error': error})


def task(request):


    return render(request, "MAIN/task.html")







@login_required
def statistic(request):
    user = request.user
    todo = Task.objects.filter(status="todo").count()
    in_progress = Task.objects.filter(status="in_progress").count()
    done = Task.objects.filter(status="done").count()
    total_tasks = todo + in_progress + done
    done_percentage = round(done / total_tasks * 100, 1) if total_tasks > 0 else 0
    projects_count = Project.objects.count()

    context = {
        "user": user,
        "todo": todo,
        "in_progress": in_progress,
        "done": done,
        "total_tasks": total_tasks,
        "done_percentage": done_percentage,
        "projects_count": projects_count,
    }
    return render(request, "OTHER/statistic.html", context)

















class TaskDetailView(DetailView):
    model = Task
    template_name = 'CRUD/task_detail.html'
    context_object_name = 'task'

class TaskUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'CRUD/task_form.html'
    success_url = reverse_lazy('task')
    permission_required = 'main.change_task'

class TaskCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'CRUD/task_create.html'
    success_url = reverse_lazy('task')
    permission_required = 'main.add_task'

class TaskDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Task
    template_name = 'OTHER/task_confirm_delete.html'
    success_url = reverse_lazy('task')
    permission_required = 'main.delete_task'




class ProjectCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'CRUD/project_create.html'
    success_url = reverse_lazy('project')
    permission_required = 'main.add_project'


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'CRUD/project_detail.html'
    context_object_name = 'project'


class ProjectUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'CRUD/project_form.html'
    success_url = reverse_lazy('project')
    permission_required = 'main.change_project'


class ProjectDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Project
    template_name = 'OTHER/project_confirm_delete.html'
    success_url = reverse_lazy('project')
    permission_required = 'main.delete_project'
