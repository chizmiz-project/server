from rest_framework import permissions

class IsAuthorOrAdmin(permissions.IsAuthenticated):

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return obj.author == request.user
