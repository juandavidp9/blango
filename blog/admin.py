from django.contrib import admin

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

    
# Register your models here.
from blog.models import Tag, Post
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)



