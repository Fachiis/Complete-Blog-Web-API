from rest_framework import permissions
from django.contrib.auth.models import User


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        #If not author of post and request is in safe methods: get, options, head
        if request.method in permissions.SAFE_METHODS:
            return True
     
        #no safe method: put, update, destroy, hence make sure the user requesting is the author of the post
        return obj.author == request.user