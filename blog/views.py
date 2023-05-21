from django.shortcuts import render
from blog.models import Post


def index(request):
    ls=Post.objects.all()
    return render (request, 'index.html', {'posts':ls})

def about(request):
    aboutPost=AboutUs.objects.all()
    return render (request, 'about.html', {'posts':aboutPost})
# Create your views here.
