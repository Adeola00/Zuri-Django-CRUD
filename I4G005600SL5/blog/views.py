from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    
class PostCreateView(CreateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")
    template_name = "blog/post_form.html"
  

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"


class PostUpdateView(UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")
    template_name = "blog/post_form.html"


class PostDeleteView(DeleteView):
    model = Post
<<<<<<< HEAD
    success_url = reverse_lazy("blog:all")
    template_name = "blog/post_confirm_delete.html"
=======
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")
    template_name = "post_confirm_delete.html"
>>>>>>> 7f647b9cc6e7508fdb52dd4f6495fb691c41af60
