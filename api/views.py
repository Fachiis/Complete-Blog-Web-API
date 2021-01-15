from django.http import request
from rest_framework import generics, permissions, viewsets
from django.contrib.auth import get_user_model

from posts.models import Post
from .serializers import PostSerializer, UserSerializer
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

'''class PostViewSet(viewsets.ModelViewSet):
    permissions_classes = [IsAuthorOrReadOnly,] #permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)'''


class UserList(generics.ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated] 
    serializer_class = UserSerializer

    def get_queryset(self):
        user = self.request.user
        username = get_user_model().objects.filter(username=user)
        return username
    

    def perform_update(self, serializer):
        user = self.request.user
        serializer.save(user=user)

