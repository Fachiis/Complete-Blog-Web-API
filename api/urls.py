from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import UserDetail, UserList, PostDetail, PostList  #PostViewSet 

#router = SimpleRouter()
#router.register('', PostViewSet, basename="posts")

urlpatterns = [
    path('', PostList.as_view()),
    path('users/', UserList.as_view()),
    path('<int:pk>/', PostDetail.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
] #+ router.urls
