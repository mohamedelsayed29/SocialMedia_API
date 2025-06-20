from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from socialmedia_api.views import PostViewSet, CommentViewSet, LikeViewSet, FollowViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'likes', LikeViewSet)
router.register(r'follows', FollowViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include('socialmedia_api.urls')),  # App URLs
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
    path('posts/<int:post_pk>/comments/', CommentViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
]
