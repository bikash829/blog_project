from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,template_name="blog_app/index.html")


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
