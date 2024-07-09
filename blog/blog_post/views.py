from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.http import JsonResponse
from django.contrib.auth.decorators import permission_required
from django.views.decorators.csrf import csrf_exempt
from . import models
from .forms import BlogPostForm

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

@csrf_exempt
def upload_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        img = models.image_upload.objects.create(image=image)
        return JsonResponse({'url':img.image.url})
    
def Logoutview(request):
    logout(request)
    return redirect("/")

def ViewSinglePost(request,pk):
    post = models.Blog_Post.objects.get(pk=pk)
    comments = post.comments.all()
    return render(request=request, template_name="singlepostview.html", context={'post':post, 'comments': comments})