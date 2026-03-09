from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().select_related('category') # Optimization: select_related avoids N+1
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    # Advanced Filtering and Search
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {
        'category__name': ['exact'],
        'price': ['gte', 'lte'],
        'stock_quantity': ['gt'], # Logic for "Stock Availability"
    }
    search_fields = ['name', 'description'] # Partial match requirement
    ordering_fields = ['price', 'created_date']
    


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

