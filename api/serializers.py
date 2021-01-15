from rest_framework import serializers
from django.contrib.auth import get_user_model

from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')


    class Meta:
        model = Post
        fields = ['id','author', 'title', 'body', 'updated_at']


class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email']