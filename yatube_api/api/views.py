from rest_framework import viewsets, filters
from django.shortcuts import get_object_or_404
from posts.models import Post, Group
from .serializers import (PostSerializer, FollowSerializer, CommentSerializer,
                          GroupSerializer)
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import permissions, mixins


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class GetCreateViewSet(mixins.CreateModelMixin,
                       mixins.ListModelMixin,
                       viewsets.GenericViewSet):
    pass


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # Максим, тут же установлен пермишн в settings (IsAuthenticatedOrReadOnly),
    # поэтому в классах я указываю только кастомный пермишн там, где он нужен.
    # По ТЗ гет запросы анонимам разрешены (кроме Follow)
    # PS: этот комммент удалю)
    permission_classes = (IsAuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly,)

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        return post.comments

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        serializer.save(
            author=self.request.user,
            post=post
        )


class FollowViewSet(GetCreateViewSet):
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        # а здесь .all() разве не будет лишнимм?)
        return self.request.user.user

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
