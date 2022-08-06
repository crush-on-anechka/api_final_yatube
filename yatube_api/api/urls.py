from django.urls import include, path
from rest_framework import routers
from .views import PostViewSet, FollowViewSet, CommentViewSet, GroupViewSet


v1_router = routers.DefaultRouter()
v1_router.register(r'v1/posts', PostViewSet)
v1_router.register(r'v1/groups', GroupViewSet)
v1_router.register(r'v1/follow', FollowViewSet, basename='follow')
v1_router.register(r'^v1/posts/(?P<post_id>\d+)/comments',
                   CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(v1_router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
