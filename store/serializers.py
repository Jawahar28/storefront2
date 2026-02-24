from rest_framework import serializers
from store.models import Product, Collection
from decimal import Decimal

class CollectionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length = 255)

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length = 255)
    unit_price = serializers.DecimalField(max_digits=6, decimal_places= 2)
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')

    # One way of relating serializers with primary keys
    '''collection = serializers.PrimaryKeyRelatedField(
        queryset = Collection.objects.all()
    )'''

    # Other Way is serialzing with string
    '''collection = serializers.StringRelatedField()'''

    # Another way is serializing with including a nested object
    '''collection = CollectionSerializer()'''

    # Another way is serializing with the hyperlink
    collection = serializers.HyperlinkedRelatedField(
        queryset = Collection.objects.all(),
        view_name = 'collection-detail',
    )


    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)