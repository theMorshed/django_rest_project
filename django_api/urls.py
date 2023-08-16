from django.urls import path, include
from rest_framework import routers
from django_api.views import ProductViewSet, ProductReviewViewSet

router = routers.DefaultRouter()
router.register('products', ProductViewSet, basename='product')
router.register('reviews', ProductReviewViewSet, basename='product_review')

urlpatterns = [
    path('', include(router.urls)),
]
