from rest_framework import serializers
from main_app.models import OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    customer_name = serializers.ReadOnlyField(source='order.user.name')
    product_name  = serializers.ReadOnlyField(source='product.name')

    class Meta:
        model  = OrderItem
        fields = ['id', 'order', 'customer_name', 'product_name', 'quantity']
