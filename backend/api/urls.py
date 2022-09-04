from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import FollowApiView, FollowListAPIView, IngredientsViewSet, RecipeViewSet, TagsViewSet

router_v1 = DefaultRouter()
router_v1.register('tags', TagsViewSet, basename='tags')
router_v1.register('ingredients', IngredientsViewSet, basename='ingredients')
router_v1.register('recipes', RecipeViewSet, basename='recipes')
router_v1.register('recipes', RecipeViewSet, basename='recipes')


urlpatterns = [
    path('users/<int:id>/subscribe/', FollowApiView.as_view(),
         name='subscribe'),
    path('users/subscriptions/', FollowListAPIView.as_view(),
         name='subscription'),
    path('auth/', include('djoser.urls.authtoken')),
    path('', include('djoser.urls')),
    path('', include(router_v1.urls)),
]