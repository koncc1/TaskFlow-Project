from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django import forms


class RegisterForm(UserCreationForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all(), 
                                   required=True, )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']