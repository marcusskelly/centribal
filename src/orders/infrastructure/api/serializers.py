from rest_framework import serializers


class OrderItemSerializer(serializers.Serializer):

    reference = serializers.CharField()
    quantity = serializers.IntegerField()


class OrderSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    items = OrderItemSerializer(many=True)
    total_without_tax = serializers.FloatField(read_only=True)
    total_with_tax = serializers.FloatField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)