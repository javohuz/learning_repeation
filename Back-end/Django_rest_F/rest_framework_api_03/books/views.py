from django.shortcuts import render
from .models import Book
from django.views.generic import ListView
# Create your views here.

class BookListView(ListView):
    model = Book
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.all()  # or whatever
        return context
