from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (FavoriteView, SubscribeView, ShoppingCartView,
                    ShowSubscriptionsView, IngredientsViewSet,
                    RecipeViewSet, TagsViewSet)

router_v1 = DefaultRouter()
router_v1.register('tags', TagsViewSet, basename='tags')
router_v1.register('ingredients', IngredientsViewSet, basename='ingredients')
router_v1.register('recipes', RecipeViewSet, basename='recipes')


urlpatterns = [
    path('recipes/<int:id>/shopping_cart/', ShoppingCartView.as_view(),
         name='shopping_cart'),
    path('recipes/<int:id>/favorite/', FavoriteView.as_view(),
         name='favorite'),
    path('users/<int:id>/subscribe/', SubscribeView.as_view(),
         name='subscribe'),
    path('users/subscriptions/', ShowSubscriptionsView.as_view(),
         name='subscription'),
    path('auth/', include('djoser.urls.authtoken')),
    path('', include('djoser.urls')),
    path('', include(router_v1.urls)),
]
