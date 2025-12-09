# main/context_processors.py
from .models import Project

def projects_context(request):
    if request.user.is_authenticated:
        user_projects = Project.objects.filter(manager=request.user)
    else:
        user_projects = Project.objects.none()  # якщо користувач неавторизований

    return {
        'projects': user_projects
    }