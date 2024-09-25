from django.urls import path
from blog_app import views

app_name  = 'blog'
urlpatterns = [
    path('', views.home, name="home"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('dashboard/',views.dashboard,name="dashboard"),
]