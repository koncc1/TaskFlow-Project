from django import forms
from .models import Ad
from django.forms import ModelForm, Textarea, TextInput, DateTimeInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group


class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['title', 'description', 'photo', 'price', 'category']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter ad title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Enter ad description'
            }),
            'photo': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter price'
            }),
            'category': forms.Select(attrs={
                'class': 'form-select'
            }),
        }




class RegisterForm(UserCreationForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all(), 
                                   required=True, 
                                   label='CHOOSE USER ROLE',)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'group']