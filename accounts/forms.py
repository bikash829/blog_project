from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User
from blog_project.custom_forms_templates import CustomFormRenderer


class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        widgets = {
            'username' : forms.TextInput(attrs={'class': 'form-control'}),
            'first_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'last_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'email' : forms.EmailInput(attrs={'class': 'form-control'}),
            'password1' : forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2' : forms.PasswordInput(attrs={'class': 'form-control'}),
        }

        # Override the init method to add 'is-invalid' class to fields with errors
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.renderer = CustomFormRenderer() # Custom form renderer
        

        for field_name, field in self.fields.items():
            if self[field_name].errors:
                field.widget.attrs.update({'class': 'form-control is-invalid'})
            else:
                field.widget.attrs.update({'class': 'form-control'})


