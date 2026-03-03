from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register()

urlpatterns = [
    # Generic/API/Class Views URLs
    # path('products/', views.ProductList.as_view()),
    # path('products/<int:id>/', views.ProductDetail.as_view()), # To view details, we should add the parameter.
    # path('collections/', views.CollectionDetail.as_view()),
    # path('collections/<int:pk>/', views.CollectionDetail.as_view()),

    # Function View/ Model View URLs
    # path('collections/', views.collection_list),
    # path('collections/<int:pk>', views.collection_detail, name='collection_detail')

    # View-Sets URLs
]
