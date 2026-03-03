from django.urls import path, include
from . import views
from rest_framework.routers import SimpleRouter
# from pprint import pprint

router = SimpleRouter()
router.register('products',views.ProductViewSet)
router.register('collections',views.CollectionViewSet)
# pprint(router.urls)

# One way of Giving URL for View Sets
# urlpatterns = router.urls


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
    path('', include(router.urls))
]
