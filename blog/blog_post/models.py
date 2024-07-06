from django.db import models
from django.contrib.auth.models import User
from django_quill.fields import QuillField


class Blog_Post(models.Model):
    title = models.CharField(max_length=255)
    post_date = models.DateField(auto_now=True)
    edit_date = models.DateField(auto_now_add=True)
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    post_image = models.ImageField(upload_to="static", null=True)
    blog_post = QuillField()

class Like(models.Model):
    count = models.IntegerField()

class image_upload(models.Model):
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    uploaded = models.DateField(auto_now=True)

class Comment(models.Model):
    comment_text = models.TextField(max_length=1000, null=False)
    date_posted = models.DateField(auto_now=True)
    post = models.ForeignKey(Blog_Post, on_delete=models.CASCADE)
    commentor = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    likes = models.ForeignKey(Like, on_delete=models.CASCADE)