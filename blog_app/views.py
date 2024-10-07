from django.shortcuts import render
from .models import Post
from .forms import ContactForm
from django.contrib import messages
# Create your views here.
def home(request):
    posts = Post.objects.all()

    template_name = "blog_app/index.html"
    context = {
        "posts": posts,
    }

    return render(request,template_name,context)


def about(request):

    template_name = "blog_app/pages/about.html"
    context = {
        
    }
    return render(request,template_name=template_name, context=context)


def contact(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            form = None
            messages.success(request,"You query has been sent successfully.")
    template_name = "blog_app/pages/contact.html"
    context={
        'form': form
    }
    
    return render(request,template_name=template_name,context=context)


def dashboard(request):

    template_name = "blog_app/pages/dashboard.html"
    context = {
        
    }
    return render(request,template_name=template_name, context=context)
