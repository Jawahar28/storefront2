from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list),
    path('products/<int:id>/', views.product_detail), # To view details, we should add the parameter.
    path('collections/<int:pk>/', views.collection_detail, name='collection-detail'),
]
