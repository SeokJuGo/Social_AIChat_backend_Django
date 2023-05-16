from rest_framework import serializers
from .models import Post
from users.serializers import TinyUserSerializer




class PostListSerializer(serializers.ModelSerializer):
    
    class Meta:
        owner = TinyUserSerializer(read_only=True)
        model = Post
        fields = "__all__"

