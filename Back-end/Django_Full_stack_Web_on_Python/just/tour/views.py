from django.shortcuts import render
from .models import Books
from django.views.generic import DetailView , ListView
# Create your views here.

class ViewBook(ListView):
    model = Books
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Books.objects.all()  # or whatever
        return context
