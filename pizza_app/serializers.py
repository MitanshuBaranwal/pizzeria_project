from rest_framework import serializers
from .models import Order, OrderStatus

class OrderSerializer(serializers.ModelSerializer):
    toppings = serializers.ListField(child=serializers.CharField(max_length=255), required=False)
    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        #print(validated_data)
        order = Order.objects.create(**validated_data)
        return order

class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = '__all__'
