from django.shortcuts import render
from .models import Post
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

    template_name = "blog_app/pages/contact.html"
    context = {
        
    }
    return render(request,template_name=template_name, context=context)


def dashboard(request):

    template_name = "blog_app/pages/dashboard.html"
    context = {
        
    }
    return render(request,template_name=template_name, context=context)
