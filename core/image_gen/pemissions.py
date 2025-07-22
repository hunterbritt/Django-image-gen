from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Allow full access to the owner, read-only to other users"
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user


# class HasAPIKey(permissions.BasePermission):
#     """
#     API key authentication decorator
#     """

#     def has_object_permission(self, request,view):
#         api_key = request.headers.get("X-API-KEY")
#         return api_key == 'YOUR'