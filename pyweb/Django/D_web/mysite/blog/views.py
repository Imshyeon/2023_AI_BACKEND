from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post
from .forms import PostForm

# Create your views here.
def home(request):
    posts=Post.object.all()
    context = {'posts':posts}
    return render(request,'blog/homepage.html',context)