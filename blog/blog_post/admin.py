from django.contrib import admin
from .models import Blog_Post,Comment,image_upload

# Register your models here.


admin.site.register(Blog_Post)
admin.site.register(Comment)
admin.site.register(image_upload)

class QuillPostAdmin(admin.ModelAdmin):
    pass
