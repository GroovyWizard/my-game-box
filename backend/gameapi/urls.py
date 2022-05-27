from django.contrib import admin
from django.urls import include, path
from users.viewsets import LoginViewSet, RegistrationViewSet, UserViewSet, RegisterSerializer, RefreshViewSet
from rest_framework import routers
from games import views
from django.conf.urls import url
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router = routers.DefaultRouter()
router.register(r'games', views.GameViewSet)
router.register(r'auth/login', LoginViewSet, basename='auth-login')
router.register(r'auth/register', RegistrationViewSet, basename='auth-register')
router.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')

# USER
router.register(r'user', UserViewSet, basename='user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/game/list/', views.GameListApi.as_view(), name="api_game_list"),
    url('api/auth/token/obtain/', TokenObtainPairView.as_view()),
    url('api/auth/token/refresh/', TokenRefreshView.as_view()),
]
