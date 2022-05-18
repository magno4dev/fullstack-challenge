from rest_framework import routers, serializers, viewsets

from order.models import Pedido
from order.models import Category

# Serializers define the API representation.
class OrderSerializer(serializers.HyperlinkedModelSerializer):
    
    category = serializers.StringRelatedField(
        many=False
    )

    class Meta:
        model = Pedido
        fields = ['id', 'contact_name', 
                    'contact_tel', 'order_description', 
                    'real_state_agency', 'company', 
                    'dead_line', 'category', 'created_on']

# Serializers define the API representation.
class CategorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'description', 'created']
