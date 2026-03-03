from django.db.models import Count
from .models import Product,Collection, OrderItem, Review
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# API Views
from rest_framework.views import APIView
# Serializers
from .serializers import ProductSerializer, CollectionSerializer, ReviewSerializer

# Mixins
from rest_framework.mixins import ListModelMixin, CreateModelMixin

# Generic Views
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# View-Sets Module
from rest_framework.viewsets import ModelViewSet

# Create your views here.
# Creating API Views.
'''@api_view()
def product_list(request):
    return Response('Okay!')

@api_view()
def product_detail(request,id):
    return Response(id)'''

# Creating Serializers Objects
'''@api_view()
def product_list(request):
    queryset = Product.objects.all()
    serializer = ProductSerializer(
        queryset, many=True,
        context={'request': request}
        )
    return Response(serializer.data)
@api_view()
def product_detail(request, id):
    # Since it is time taking process we use django shortcuts
    # try:
    #     product = Product.objects.get(pk=id)
    #     serializer = ProductSerializer(product)
    #     return Response(serializer.data)
    # except Product.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)

    product = get_object_or_404(Product, pk=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)

@api_view()
def collection_detail(request, pk):
    return Response('Ok')
'''

'''@api_view(['GET','POST'])
def product_list(request):
    if request.method == 'GET':
        queryset = Product.objects.all()
        serializer = ProductSerializer(
            queryset, many=True,
            context={'request': request}
            )
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.validated_data
        #     return Response('Ok')
        # else:
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Another Form of Validating Data
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # print(serializer.validated_data)
        return Response(serializer.data, status = status.HTTP_201_CREATED)'''

# Saving Object in the database
'''@api_view(['GET','PUT','PATCH','DELETE'])
def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == 'GET': 
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    # Deleting Items in the database using API
    elif request.method == 'DELETE':
        if product.orderitem_set.count() > 0:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)'''
    

'''@api_view()
def collection_detail(request, pk):
    return Response('Ok')'''


# Exercise

# Printing all Collections
'''@api_view()
def collection_list(request):
    queryset = Collection.objects.all()
    serializer = CollectionSerializer(
        queryset, many = True
    )
    return Response(serializer.data)'''

# Priting all collections with products_count
'''@api_view(['GET','POST'])
def collection_list(request):
    if request.method == 'GET':
        queryset = Collection.objects.annotate(products_count = Count('products')).all()
        serializer = CollectionSerializer(
            queryset, many = True
        )
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CollectionSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)'''
    

'''@api_view(['GET','PUT','DELETE'])
def collection_detail(request,pk):
    collection = get_object_or_404(
        Collection.objects.annotate(
            products_count = Count('products')),
            pk = pk)

    if request.method == 'GET':
        serializer = CollectionSerializer(collection)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method =='DELETE':
        if collection.products.count() > 0:
            return Response({'error': 'Collection cannot be delete'}, status = status.HTTP_405_METHOD_NOT_ALLOWED)
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)'''

# Class Based Views
'''class ProductList(APIView):
    def get(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(
            queryset, many=True,
            context={'request': request}
            )
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # print(serializer.validated_data)
        return Response(serializer.data, status = status.HTTP_201_CREATED)

class ProductDetail(APIView):
    def get(self, request, id):
        product = get_object_or_404(Product, pk=id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    def put(self, request,id):
        product = get_object_or_404(Product, pk = id)
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request,id):
        product = get_object_or_404(Product, pk=id)
        if product.orderitem_set.count() > 0:
            return Response(f"Product Cannot be deleted", status=status.HTTP_405_METHOD_NOT_ALLOWED)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)'''


# Generic Views ( Concreate Class Views)

'''class ProductList(ListCreateAPIView):
    def get_queryset(self):
        return Product.objects.select_related('collection').all()
    
    def get_serializer_class(self):
        return ProductSerializer
    
    def get_serializer_context(self):
        return {'request' : self.request}'''


'''class ProductDetail(APIView):
    def get(self, request, id):
        product = get_object_or_404(Product, pk=id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    def put(self, request,id):
        product = get_object_or_404(Product, pk = id)
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request,id):
        product = get_object_or_404(Product, pk=id)
        if product.orderitem_set.count() > 0:
            return Response(f"Product Cannot be deleted", status=status.HTTP_405_METHOD_NOT_ALLOWED)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)'''

        
# Exercise
'''class CollectionDetail(ListCreateAPIView):
    def get_queryset(self):
        return Collection.objects.annotate(products_count = Count('products')).all()
    
    def get_serializer_class(self):
        return CollectionSerializer
    
    def get_serializer_context(self):
        return {'request' : self.request}'''


# Customizing Generic Views
'''class ProductDetail(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'
    
    def delete(self, request,id):
        product = get_object_or_404(Product, pk=id)
        if product.orderitem_set.count() > 0:
            return Response(f"Product Cannot be deleted", status=status.HTTP_405_METHOD_NOT_ALLOWED)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)'''

'''class CollectionDetail(RetrieveUpdateDestroyAPIView):
    queryset = Collection.objects.annotate(products_count = Count('products')).all()
    serializer_class = CollectionSerializer

    def delete(self, request, pk):
        collection = get_object_or_404(Collection, pk = pk)
        if collection.products.count() > 0:
            return Response({'error': 'Collection cannot be delete'})
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) '''
    
# View Sets
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get_serializer_context(self):
        return {'request' : self.request}
    
    def destroy(self, request, *args, **kwargs):
        if OrderItem.objects.filter(product_id= kwargs['pk']).count() > 0:
            return Response(f"Product Cannot be deleted", status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request, *args, **kwargs)
    
class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.annotate(products_count = Count('products')).all()
    serializer_class = CollectionSerializer

    # def get_serializer_context(self):
    #     return {'request': self.request}

    def destroy(self, request, *args, **kwargs):
        if Collection.objects.filter(id = kwargs['pk'], products__isnull=False).count() > 0:
            return Response({'error :'"Collection can't be deleted"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request, *args, **kwargs)
    
class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    
    