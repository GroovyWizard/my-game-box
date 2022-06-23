from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import routers
from games import views
from users import views as user_views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

router = routers.DefaultRouter()
router.register(r'games', views.GameViewSet)
router.register(r'users', user_views.UserViewSet)
router.register(r'favorites', views.FavoriteViewSet)
router.register(r'played', views.PlayedViewSet)
router.register(r'playing', views.PlayingViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="My Game Box Game API",
      default_version='v1',
   ),
   public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/game/list/', views.GameListApi.as_view(), name="api_game_list"),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
