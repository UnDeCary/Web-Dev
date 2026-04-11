from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet
import views

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('products/', views.generics.ProductListAPIView.as_view()),
    path('products/<int:product_id>/', views.generics.ProductDetailAPIView.as_view()),

    path('categories/', views.generics.CategoryListAPIView.as_view()),
    path('categories/<int:category_id>/', views.generics.CategoryDetailAPIView.as_view()),
    path('categories/<int:category_id>/products/', views.generics.CategoryProductsAPIView.as_view()),
]