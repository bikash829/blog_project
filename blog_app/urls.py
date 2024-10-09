from django.urls import path
from blog_app import views

app_name  = 'blog'
urlpatterns = [
    path('', views.home, name="home"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('create_post/',views.create_post,name="create_post"),
    path('edit_post/<int:id>/',views.edit_post,name="edit_post"),
    path('delete_post/<int:id>/',views.delete_post,name="delete_post"),
]