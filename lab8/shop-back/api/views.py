from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Product, Category

from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import CategorySerializer, ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(detail=True, methods=['get'])
    def products(self, request, pk=None):
        category = self.get_object()
        products = Product.objects.filter(category=category)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['price', 'name', 'id']
    ordering = ['id']

    search_fields = ['name', 'description']

    def get_queryset(self):
        queryset = Product.objects.all()

        category_id = self.request.query_params.get("category")
        is_active = self.request.query_params.get("is_active")
        search = self.request.query_params.get("search")

        if category_id:
            queryset = queryset.filter(category_id=category_id)

        if is_active:
            is_active = is_active.lower() == 'true'
            queryset = queryset.filter(is_active=is_active)

        if search:
            queryset = queryset.filter(name__icontains=search)

        return self.filter_queryset(queryset)

    @action(detail=False, methods=["get"])
    def active(self, request):
        active_products = Product.objects.filter(is_active=True)
        filtered_active = self.filter_queryset(active_products)
        serializer = self.get_serializer(filtered_active, many=True)
        return Response(serializer.data)