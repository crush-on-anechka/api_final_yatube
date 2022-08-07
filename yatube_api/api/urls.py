from django.urls import include, path
from rest_framework import routers
from .views import PostViewSet, FollowViewSet, CommentViewSet, GroupViewSet
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView,
                                            TokenVerifyView)


v1_router = routers.DefaultRouter()
v1_router.register(r'posts', PostViewSet)
v1_router.register(r'groups', GroupViewSet)
v1_router.register(r'follow', FollowViewSet, basename='follow')
v1_router.register(r'^posts/(?P<post_id>\d+)/comments',
                   CommentViewSet, basename='comment')

jwt_patterns = [
    path('create/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify/', TokenVerifyView.as_view(), name='token_verify'),
]

urlpatterns = [
    path('', include(v1_router.urls)),
    path('jwt/', include(jwt_patterns))
]
