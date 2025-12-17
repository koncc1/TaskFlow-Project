# main/context_processors.py
from .models import Project, Task
from django.utils.timezone import now


def projects_context(request):
    if request.user.is_authenticated:
        user_projects = Project.objects.filter(manager=request.user)
    else:
        user_projects = Project.objects.none()

    return {
        'projects': user_projects
    }

def tasks_context(request):
    if not request.user.is_authenticated:
        return {}

    status_filter = request.GET.get('status', 'all')
    extra_filter = request.GET.get('filter')


    tasks = Task.objects.filter(assignee=request.user)


    if extra_filter == 'overdue':
        tasks = tasks.filter(
        deadline__lt=now()
        ).exclude(status='done')


    if status_filter != 'all':
        tasks = tasks.filter(status=status_filter)


    columns = []
    for status, label in Task.STATUS_CHOICES:
        columns.append({
            'status': status,
            'label': label,
            'tasks': tasks.filter(status=status)
        })

    return {
        'columns': columns,
        'current_status': status_filter,
        'current_filter': extra_filter,
        'status_choices': Task.STATUS_CHOICES,
    }