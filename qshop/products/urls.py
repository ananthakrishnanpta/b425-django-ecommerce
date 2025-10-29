from django.urls import path

from .views import ViewProducts, AddProduct, ProductDetail

urlpatterns = [
    path('', ViewProducts.as_view(), name='view_products'),
    path('add/', AddProduct.as_view(), name = 'add_product'),
    path('<int:pk>/', ProductDetail.as_view(), name = 'prod_detail')
]