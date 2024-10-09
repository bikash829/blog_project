from django.shortcuts import redirect, render,get_object_or_404
from .models import Post
from .forms import ContactForm,PostForm
from django.contrib import messages
from blog_project.custom_forms_templates import BootstrapErrorList
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
    posts = Post.objects.all()
    template_name = "blog_app/pages/dashboard.html"
    context = {
        'posts': posts,
    }
    return render(request,template_name=template_name, context=context)



def create_post(request):
    form = PostForm(error_class=BootstrapErrorList)
    if request.method == 'POST':
        form = PostForm(request.POST,error_class=BootstrapErrorList)
        if form.is_valid():
            form.save()
            messages.info(request,"Post has been created successfully.")
            return redirect('blog:dashboard')

    template_name = "blog_app/pages/create_blog.html"
    context = {
        'form': form,
    }
    return render(request,template_name,context)


def edit_post(request,id):
    post = get_object_or_404(Post,id=id)
    # initial_data = {
    #     'title': post.title,
    #     'description': post.description,
    # }
    form = PostForm(error_class=BootstrapErrorList,instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST,error_class=BootstrapErrorList)
        if form.is_valid():
            form.save()
            messages.info(request,"Post has been updated successfully.")
            return redirect('blog:dashboard')

    template_name = "blog_app/pages/create_blog.html"
    context = {
        'form': form,
    }
    return render(request,template_name,context)



def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    
    if post:
        post.delete()
        messages.success(request, "Post has been deleted successfully.")
        return redirect('blog:dashboard')
    else:
        messages.warning(request, "Technical error couldn't delete the post")
        return redirect('blog:dashboard')
    
    # template_name = "blog_app/pages/confirm_delete.html"
    # context = {
    #     'post': post,
    # }
    # return render(request, template_name, context)