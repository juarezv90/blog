from typing import Any
from django.forms import ModelForm
from django import forms
from .models import Blog_Post, Comment
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class BlogPostForm(ModelForm):
    class Meta:
        model = Blog_Post
        fields = ["title" , "post_image", "blog_post"]

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["comment_text"]

class AddUserForm(UserCreationForm):
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')

    class Meta:
        model = User
        fields=('username','first_name','last_name',)
        fieldsets = (
            (None, {
                'fields': (
                    'username','email','password1','password2'
                ),
            }),
        )
    def save(self, commit=True):
        user = super(AddUserForm, self).save(commit=False)
        user.first_name = self.changed_data['first_name']
        user.last_name = self.changed_data['last_name']
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
    
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

class LoginForm(AuthenticationForm):
    pass
