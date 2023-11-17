from django.shortcuts import render
from django.views.generic import ListView
from .models import NewPost
# Create your views here.
class HomePage(ListView):
    model = NewPost
    template_name = 'home.html'