from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from games import views


router = routers.DefaultRouter()
router.register(r'games', views.GameViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/game/list/', views.GameListApi.as_view(), name="api_game_list")
]
