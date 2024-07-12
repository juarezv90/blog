from django.urls import path
from . import views

urlpatterns = [
    path("", views.Index, name="home"),
    path("post/", views.PostRequest, name="post"),
    path("upload_image/", views.upload_image, name="upload_image"),
    path("login/", views.LoginView, name="login"),
    path("logout/", views.Logoutview, name="logout"),
    path("post/<int:pk>", views.ViewSinglePost, name="postview"),
    path("post/likepost/<int:pk>", views.BlogPostLike, name="like_post"),
    path("post-comment/<int:pk>", views.AddComment, name="addcomment"),
    path("signup/", views.CreateUser, name="signup")
]