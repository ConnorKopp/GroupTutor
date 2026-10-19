from django import forms  
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "first_name", "last_name", "email", "is_ta", "bio", "courses")  
        widgets = {"courses": forms.CheckboxSelectMultiple}  

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "first_name", "last_name", "is_ta", "bio", "courses")  

class TAProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "bio", "courses")
        widgets = {"courses": forms.CheckboxSelectMultiple}