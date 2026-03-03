from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductList.as_view()),
    path('products/<int:id>/', views.ProductDetail.as_view()), # To view details, we should add the parameter.
    path('collections/', views.CollectionDetail.as_view()),
    path('collections/<int:pk>/', views.CollectionDetail.as_view()),
#     path('collections/', views.collection_list),
#     path('collections/<int:pk>', views.collection_detail, name='collection_detail')
]
