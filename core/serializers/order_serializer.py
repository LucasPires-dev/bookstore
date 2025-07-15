from rest_framework import serializers
from django.contrib.auth.models import User
from core.models.order import Order, OrderItem
from core.models.product import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'price']


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), source='product', write_only=True
    )

    class Meta:
        model = OrderItem
        fields = ['product', 'product_id', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    items = OrderItemSerializer(source='orderitem_set', many=True)

    class Meta:
        model = Order
        fields = ['id', 'order_number', 'user', 'status', 'items', 'created_at', 'updated_at']
        read_only_fields = ['order_number', 'created_at', 'updated_at']

    def create(self, validated_data):
        items_data = validated_data.pop('orderitem_set')
        order = Order.objects.create(**validated_data)  # ← Remova o `user=...`

        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)

        return order
