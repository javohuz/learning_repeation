from django.urls import path
from .views import PostListApiView , PostDetailView

urlpatterns = [
    path('<int:pk>/', PostDetailView.as_view()),
    path('', PostListApiView.as_view()),
]