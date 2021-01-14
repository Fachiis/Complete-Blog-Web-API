from rest_framework import generics, permissions

from posts.models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthorOrReadOnly, permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)
