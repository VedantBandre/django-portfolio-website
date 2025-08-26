from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    context = {}
    # return HttpResponse('<h2>Home</h2>')
    return render(request, 'base/main.html', context)

def posts(request):
    context = {}
    # return HttpResponse('<h2>Posts</h2>')
    return render(request, 'base/home.html', context)

def post(request):
    context = {}
    # return HttpResponse('<h2>Post Title</h2>')
    return render(request, 'base/home.html', context)

def profile(request):
    context = {}
    # return HttpResponse('<h2>User</h2>')
    return render(request, 'base/home.html', context)