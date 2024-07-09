from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.Index, name="home"),
    path("post/", views.PostRequest, name="post"),
    path("upload_image/", views.upload_image, name="upload_image"),
    path("login/", auth_views.LoginView.as_view(template_name="login.html", next_page="home"), name="login"),
    path("logout/", views.Logoutview, name="logout"),
    path("post/<int:pk>", views.ViewSinglePost, name="postview"),
]