from rest_framework.permissions import BasePermission


class IsDirectorPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user is not None and request.user.role == "D"
