from django.db import models
from django.contrib.auth.models import User


class Blog_Post(models.Model):
    title = models.CharField(max_length=255)
    post_date = models.DateField(auto_now=True)
    edit_date = models.DateField(auto_now_add=True)
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    blog_post = models.TextField(max_length=2000)

class Like(models.Model):
    count = models.IntegerField()

class Comment(models.Model):
    comment_text = models.TextField(max_length=1000, null=False)
    date_posted = models.DateField(auto_now=True)
    post = models.ForeignKey(Blog_Post, on_delete=models.CASCADE)
    commentor = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    likes = models.ForeignKey(Like, on_delete=models.CASCADE)