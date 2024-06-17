from django.forms import ModelForm
from .models import Blog_Post, Comment

class BlogPostForm(ModelForm):
    class Meta:
        model = Blog_Post
        fields = ["title", "blog_post"]

form = BlogPostForm()