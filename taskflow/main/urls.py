from django.urls import path
from . import views 
from .views import project,register, logout_view, task, statistic
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView, LoginView
from .views import ProjectDeleteView,  TaskCreateView, ProjectCreateView,ProjectUpdateView, TaskDetailView,TaskUpdateView,TaskDeleteView,ProjectDetailView



urlpatterns = [
    path('', views.home, name='home'),
    path('project/',project , name='project'),
    path('task/', task, name='task'),
    


    path('statistic/', statistic , name='statistic'),

    

    #CRUD проєкстс
    path('project/create/', ProjectCreateView.as_view(), name='CRUD/project'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'), 
    path('project/<int:pk>/edit/', ProjectUpdateView.as_view(), name='project_edit'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),

    #CRUD TASKIIIII
    path('task/create/', TaskCreateView.as_view(), name='CRUD/task'),
    path('task/<int:pk>/edit/', TaskUpdateView.as_view(), name='task_edit'), 
    path('task/<int:pk>/', views.task_detail_with_comments, name='task_detail'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),


    # LOGINS
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='OTHER/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),

]
