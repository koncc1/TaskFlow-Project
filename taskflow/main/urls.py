from django.urls import path
from . import views 
from .views import project,register, logout_view
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path('', views.home, name='home'),
    path('project/',project , name='project'),



    # LOGINS
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='OTHER/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),

]
