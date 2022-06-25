from cgitb import html
from dataclasses import fields
from typing import Generic
from django.shortcuts import render
from .models import Post
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from blog.templates import *


# Create your views here.


class PostListView(ListView):
    model = Post
    template_name = 'postlist.html'


class PostCreateView(CreateView):
    model = Post
    fields = '__all__'
    success_url = 'reverse_lazy("blog:all")'
    template_name = 'post_form.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class PostUpdateView(UpdateView):
    model = Post
    fields = '__all__'
    success_url = 'reverse_lazy("blog:all")'
    template_name = 'base.hmtl'


class PostDeleteView(UpdateView):
    model = Post
    fields = '__all__'
    success_url = 'reverse_lazy("blog:all")'
    template_name = 'post_confirm_delete'
