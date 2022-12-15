from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='products_list'),
    path('create/', views.createProduct, name='create_product'),
    path('update/<int:pk>/', views.updateProduct, name='update_product'),
    path('delete/<int:pk>/', views.deleteProduct, name='delete_product'),
    path('deleteimage/<int:pk>/', views.deleteImage, name='delete_image'),
    path('deletevariant/<int:pk>/', views.deleteVariant, name='delete_variant'),
]