from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .models import Ad
from .forms import AdForm, RegisterForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.contrib.auth.models import User
from django.contrib.auth import login




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
                return redirect('main')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form, 'error': error})

                 



def ad_list(request):

    ads = Ad.objects.all()


    search_data = request.GET.get('q', '').strip()
    if search_data:
        ads = ads.filter(title__icontains=search_data) 

    sort_param = request.GET.get('sort', '')
    if sort_param == 'asc':
        ads = ads.order_by('date') 
    elif sort_param == 'desc':
        ads = ads.order_by('-date') 
    elif sort_param == '-price':
        ads = ads.order_by('price') 
    elif sort_param == 'price':
        ads = ads.order_by('-price') 


    category_param = request.GET.get('category', '')
    if category_param == 'SUPERCARS':
        ads = ads.filter(category__name__iexact=category_param)
    elif category_param == 'SPORT CARS':
        ads = ads.filter(category__name__iexact=category_param)
    elif category_param == 'MUSCLE-CARS':
        ads = ads.filter(category__name__iexact=category_param)
    elif category_param == 'OFF-ROAD':
        ads = ads.filter(category__name__iexact=category_param)
    elif category_param == 'LUXURY':
        ads = ads.filter(category__name__iexact=category_param)




    return render(request, "CRUD/ad_list.html", {'ads': ads, 'q': search_data, 'sort': sort_param, 'category': category_param,})




class AdListView(ListView):
    model = Ad
    template_name = 'CRUD/ad_list.html'
    context_object_name = 'main'

class AdDetailView(DetailView):
    model = Ad
    template_name = 'CRUD/ad_detail.html'
    context_object_name = 'ad'


class AdCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Ad
    form_class = AdForm
    template_name = 'CRUD/ad_form.html'
    success_url = reverse_lazy('ad_list')
    permission_required = 'main.add_ad'


class AdUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Ad
    form_class = AdForm
    template_name = 'CRUD/ad_form.html'
    success_url = reverse_lazy('ad_list')
    permission_required = 'main.change_ad'


class AdDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Ad
    template_name = 'CRUD/ad_confirm_delete.html'
    success_url = reverse_lazy('ad_list')
    permission_required = 'main.delete_ad'
