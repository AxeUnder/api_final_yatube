# TODO:  Напишите свой вариант
from rest_framework import viewsets, filters, permissions, pagination
from rest_framework.generics import get_object_or_404

from posts.models import Post, Group

from .serializers import (PostSerializer, CommentSerializer, GroupSerializer,
                          FollowSerializer)
from .permissions import IsAuthorOrReadOnlyPermission


class PostViewSet(viewsets.ModelViewSet):
    """ViewSet модели Post."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAuthorOrReadOnlyPermission)
    pagination_class = pagination.LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """ViewSet модели Comment."""
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAuthorOrReadOnlyPermission)

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        return post.comments.all()

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            post=get_object_or_404(Post, id=self.kwargs.get('post_id'))
        )


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet модели Group."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FollowViewSet(viewsets.ModelViewSet):
    """ViewSet модели Follow."""
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username', 'user__username')

    def get_queryset(self):
        return self.request.user.follower

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
