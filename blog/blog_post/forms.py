from django.forms import ModelForm
from .models import Blog_Post, Comment
from django.contrib.auth.models import User

class BlogPostForm(ModelForm):
    class Meta:
        model = Blog_Post
        fields = ["title", "blog_post", "post_image"]
