from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User


class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        # fields = '__all__'


