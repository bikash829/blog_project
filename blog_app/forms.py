from django import forms 
from django.forms import ModelForm
from .models import Contact,Post
from blog_project.custom_forms_templates import CustomFormRenderer
class ContactForm(ModelForm):
    class Meta: 
        model = Contact
        fields = "__all__"
class PostForm(ModelForm):
    class Meta: 
        model = Post
        fields = ['title','description']

        # Override the init method to add 'is-invalid' class to fields with errors
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.renderer = CustomFormRenderer() # Custom form renderer
        

        for field_name, field in self.fields.items():
            if self[field_name].errors:
                field.widget.attrs.update({'class': 'form-control is-invalid'})
            else:
                field.widget.attrs.update({'class': 'form-control'})   