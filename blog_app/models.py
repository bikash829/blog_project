from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()


    def __str__(self):
        return self.title
    


class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=200)
    message = models.TextField()


    def __str__(self):
        return self.email