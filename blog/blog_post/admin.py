from django.contrib import admin
from .models import Blog_Post,Comment

# Register your models here.


admin.site.register(Blog_Post)
admin.site.register(Comment)

class QuillPostAdmin(admin.ModelAdmin):
    pass
