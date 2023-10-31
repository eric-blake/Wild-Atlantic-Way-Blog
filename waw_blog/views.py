from django.shortcuts import render
from django.views import generic
from .models import Post



class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.all()
    template_name = "index.html"




