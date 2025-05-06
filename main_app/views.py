from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from main_app.models import OrderItem
from main_app.serializers import OrderItemSerializer


class OrderItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = OrderItem.objects.select_related(
        'order__user',  # Fetches Order and User in single query
        'product'       # Fetches Product in same query
    ).all()
    serializer_class = OrderItemSerializer
    pagination_class = PageNumberPagination
    pagination_class.page_size = 100  # Adjust this number as needed
