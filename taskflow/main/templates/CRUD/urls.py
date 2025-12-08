from django.urls import path, include
from .views import AdDetailView, AdCreateView, AdUpdateView, AdDeleteView
from .views import ad_list, register
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', ad_list, name='ad_list'),
    path('register/', register, name='register'),

    path('ad/create/', AdCreateView.as_view(), name='ad_create'),   
    path('ad/<int:pk>/', AdDetailView.as_view(), name='ad_detail'), 
    path('ad/<int:pk>/edit/', AdUpdateView.as_view(), name='ad_edit'), 
    path('ad/<int:pk>/delete/', AdDeleteView.as_view(), name='ad_delete'),

    path('login/', auth_views.LoginView.as_view(template_name='CRUD/login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='ad_list'), name='logout'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


