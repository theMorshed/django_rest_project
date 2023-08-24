from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django_api.models import Product, ProductReview
from django_api.serializers import ProductSerializer, ProductReviewSerializer
from django_api.permissions import AdminOrReadOnly, ReviewOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

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
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['user__username']
    filterset_fields = ['rating', 'product']
    
    # def get_queryset(self):
    #     queryset = ProductReview.objects.all()
    #     username = self.request.query_params.get('username')
    #     if username is not None:
    #         queryset = queryset.filter(user__username__icontains=username)
    #     return queryset