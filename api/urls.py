from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView
)

from . import views

router = DefaultRouter()
router.register(r'posts', views.PostViewSet, basename='posts')
router.register(
    r'posts/(?P<post_id>[0-9]+)/comments', views.CommentViewSet,
    basename='comments'
)
router.register(r'follow', views.FollowViewSet, basename='follow')
router.register(r'group', views.GroupViewSet, basename='group')


urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
