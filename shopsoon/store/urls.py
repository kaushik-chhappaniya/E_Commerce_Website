from django.urls import path
from . import views

urlpatterns = [
 
    path('', views.store, name='store'),

# Indivial products
    path('product/<slug:slug>/', views.product_info, name='product-info'),

# Individual Categories
    path('search/<slug:slug>', views.list_category, name='list-category'),

    
]