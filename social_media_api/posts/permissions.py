from rest_framework import permissions

class IsAuthorOfPost(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user

class IsAuthorOfComment(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user