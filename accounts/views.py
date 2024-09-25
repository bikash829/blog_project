from django.shortcuts import render,redirect
from .forms import UserForm
# Create your views here.

def sign_up(request):
    form = UserForm()

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:home')

    template_name = "accounts/sign_up.html"
    context = {
        'form': form
    }
    return render(request,template_name,context)