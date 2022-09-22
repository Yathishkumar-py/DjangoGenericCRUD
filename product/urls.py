from django.urls import path
from .views import ProductsListView, ProductDetailView, ProductCreateView

urlpatterns = [
    path('', ProductsListView.as_view(), name='products_list'),
    path('<int:pk>/details', ProductDetailView.as_view(), name='product_detail'),
    path('create', ProductCreateView.as_view(), name='product_create'),
]
