from rest_framework import permissions


class IsAuthorOrReadOnlyPermission(permissions.BasePermission):
    """Разрешение на редактирование только для автора."""
    message = 'Пользователь не является автором!'

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)
