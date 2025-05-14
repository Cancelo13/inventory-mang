from django.urls import path
from . import views


urlpatterns = [
    path('' , views.home_view, name='home'),
    path('product/create/' , views.product_create_view, name='product_create'),
    path('product/list/' , views.product_read_view, name='product_list'),
    path('product/update/<int:pk>/', views.product_update_view, name='product_update'),
    path('product/delete/<int:pk>/', views.product_delete_view, name='product_delete'),
]