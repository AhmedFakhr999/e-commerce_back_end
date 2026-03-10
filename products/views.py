from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    
    queryset = Product.objects.all().select_related('category')
    serializer_class = ProductSerializer
    
    # Enable Filtering, Search, and Ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # Exact match for category, range for price
    filterset_fields = {
        'category__name': ['exact'],
        'price': ['gte', 'lte'],
        'stock_quantity': ['gt'], # Logic for "In Stock"
    }
    
    # Partial match for Name and Description
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'created_date']
    


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

