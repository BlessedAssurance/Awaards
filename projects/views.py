from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic import ListView, DetailView
from .models import *
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse_lazy
from .forms import PostForm,ProfileForm,UserRegisterForm
from django.views import generic
from django.db.models import Avg
# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = ' '

class PostDetailView(DetailView): 
    model = Post
    template_name = ' '

class SignUpView(generic.CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    template_name = ' '

