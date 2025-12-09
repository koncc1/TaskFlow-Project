from django.shortcuts import render,redirect
from .models import Project
from django.contrib.auth.models import User
from django.contrib.auth import login
from .forms import RegisterForm
from django.contrib.auth import logout
from django.shortcuts import redirect


def home(request):
    
    return render(request, "MAIN/home.html")

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
