from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django_api.models import Product, ProductReview
from django_api.serializers import ProductSerializer, ProductReviewSerializer
from django_api.permissions import AdminOrReadOnly, ReviewOrReadOnly

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [AdminOrReadOnly]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class ProductReviewViewSet(viewsets.ModelViewSet):
    permission_classes = [ReviewOrReadOnly]
    # permission_classes = [IsAuthenticated]
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer