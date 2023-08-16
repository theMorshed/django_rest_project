from django.contrib import admin
from django_api.models import Product, ProductReview

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'price']
@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'user', 'rating', 'review', 'created_at', 'updated_at']