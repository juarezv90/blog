from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import logout, authenticate, login
from django.http import JsonResponse
from django.contrib.auth.decorators import permission_required
from django.views.decorators.csrf import csrf_exempt
from . import models
from .forms import BlogPostForm, CommentForm, AddUserForm, LoginForm

def Index(request):
    data = models.Blog_Post.objects.all()
    return render(request, "home.html", {"posts":data})

@permission_required('blog_post.publish_post', login_url="/")
def PostRequest(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            return redirect('home')
    else:
        form = BlogPostForm()
    return render(request, "post.html", {'form':form})

def ViewSinglePost(request,pk):
    post = models.Blog_Post.objects.get(pk=pk)
    comments = post.comments.all()
    post_is_like = post.likes.filter(id=request.user.id).exists()
    form = CommentForm()
    return render(request=request, template_name="singlepostview.html", context={'post':post, 'comments': comments, 'post_is_like': post_is_like, 'comment_form': form})

@csrf_exempt
def upload_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        img = models.image_upload.objects.create(image=image)
        return JsonResponse({'url':img.image.url})
    
def Logoutview(request):
    logout(request)
    return redirect("/")

def LoginView(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form':form})

    pass


def BlogPostLike(request, pk):
    post = models.Blog_Post.objects.get(pk=pk)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect(reverse('postview', args=[str(pk)]))

def AddComment(request, pk):
    if request.method == 'POST':
        form = CommentForm(request.POST or None)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post_id = pk
            comment.save()
            form = CommentForm()
    else:
        form = CommentForm()
    return redirect(reverse('postview', args=[str(pk)]))

def CreateUser(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST or None)
        if form.is_valid():
            form.save()
        
    else:
        form = AddUserForm()
    return render(request, "joinsite.html", {'form':form})

def DashboardView(request):
    pass