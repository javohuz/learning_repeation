from .views import ViewBook
from django.urls import path

urlpatterns = [
    path('', ViewBook.as_view() , name='home')
]