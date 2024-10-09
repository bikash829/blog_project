from django.contrib import admin
from blog_app.models import Post, Contact

class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','description']

admin.site.register(Post,PostAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','address','message']
admin.site.register(Contact,ContactAdmin)