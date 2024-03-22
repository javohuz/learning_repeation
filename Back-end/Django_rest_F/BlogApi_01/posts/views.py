from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
from .models import Post
from .serializers import PostApiSerializer
# Create your views here.

class PostListApiView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostApiSerializer

class PostDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostApiSerializer