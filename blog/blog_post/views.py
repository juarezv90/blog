from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from . import models
from .forms import BlogPostForm

def Index(request):
    data = models.Blog_Post.objects.all()

    return render(request, "home.html", {"posts":data})

def PostRequest(request):
    context = {}

    form = BlogPostForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()

    context['form']=form
    return render(request, "post.html", context)

@csrf_exempt
def upload_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        img = models.image_upload.objects.create(image=image)
        return JsonResponse({'url':img.image.url})