from django.contrib import admin
from blog_app.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','description']

admin.site.register(Post,PostAdmin)
