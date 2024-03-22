from rest_framework import serializers
from .models import Post


class PostApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'auther', 'body', 'created_at', 'delete_at')