from django.shortcuts import render
from django.urls import reverse

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.utils import timezone
from .models import Post

# Create your views here.
class PostList(ListView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class PostDetail(DetailView):
    """Полное описание фильма"""
    model = Post
    slug_field = "url"

class PostUpdate(UpdateView):
    model = Post
    success_url =  'delete'
    slug_field = "url"
    fields = ['dara', 'description', 'text', 'title']
    template_name = 'later/post_update.html'



class PostCreate(CreateView): # новое изменение
    model = Post
    template_name = 'later/post_new.html'
    fields = '__all__'



class PostDelete(DeleteView):
    model = Post
    success_url = "/later/list"
    # queryset = Post.objects.filter(url='slug')
    template_name = 'later/post_delete.html'
    slug_field = "url"
