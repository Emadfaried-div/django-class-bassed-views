from django.shortcuts import render
from .models import Post
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView,UpdateView,DeleteView
from django.template.defaultfilters import last

# Create your views here.
class PostList(ListView):
    model = Post  ## to show the order in template use: [object_list] or [post_list] wihch post_list is the name of html page of post-list.html 

   # context_object_name = 'all_posts'       # <---------   if you wnat to use attributes/////......  or i can use other name to call the cbv in my template
    ordering = '-created_at'
    #queryset = Post.objects.filter(active=True) <----- if you wnat to use attributes
 
 
    def get_queryset(self):   # <----- if you want to use methods to define the queryset for filter as example 
        return Post.objects.filter(active=True)

    def get_context_data(self, **kwargs):    # <----- if you want to use methods to define the context 
        context = super().get_context_data(**kwargs)
        context[""] = ""    # use it if you want to reuturn with more an objects which not in context like a comments or activ user names ...
        return context
        

class PostDetial(DetailView):
    model = Post



class PostCreate():
    pass


class PostUpdate():
    pass


class PostDelete():
    pass
