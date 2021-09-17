from django.shortcuts import render
from .models import Product
from .serialize import ProductSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet 

# Create your views here.
class ProductViewset(ReadOnlyModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    
    