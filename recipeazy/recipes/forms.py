from django import forms
from .models import Recipe, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title','cook_time', 'servings',"difficulty","description", 'ingredients',"method","image", "cuisine", "category"]

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","email","password1","password2"]

class CreateProfile(forms.ModelForm):
    