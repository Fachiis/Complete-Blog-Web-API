from rest_framework import serializers

from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ['id','author', 'title', 'body', 'updated_at']