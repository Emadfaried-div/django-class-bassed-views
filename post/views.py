from django.shortcuts import render
from .models import Post
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView,UpdateView,DeleteView

# Create your views here.
class PostList(ListView):
    model = Post



class PostDetial(DetailView):
    model = Post



class PostCreate():
    pass


class PostUpdate():
    pass


class PostDelete():
    pass
