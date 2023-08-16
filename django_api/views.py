from django.shortcuts import render
from rest_framework import viewsets
from django_api.models import Product, ProductReview
from django_api.serializers import ProductSerializer, ProductReviewSerializer

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class ProductReviewViewSet(viewsets.ModelViewSet):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer