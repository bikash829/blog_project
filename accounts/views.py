from django.shortcuts import render,redirect
from .forms import UserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
from .custom_forms_templates import BootstrapErrorList

def sign_up(request):
    form = UserForm(error_class=BootstrapErrorList)

    if request.method == "POST":
        form = UserForm(request.POST,error_class=BootstrapErrorList)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been created successfully.")
            return redirect('blog:home')

    template_name = "registration/sign_up.html"
    context = {
        'form': form
    }
    return render(request,template_name,context)


@login_required
def profile(request):
    template_dir = "registration/profile.html"
    context= {

    }
    return render(request,template_dir,context)