from django.urls import path, include
from rest_framework.routers import DefaultRouter
from main_app.views import OrderItemViewSet

router = DefaultRouter()
router.register(r'order-item', OrderItemViewSet, basename='order_item')

urlpatterns = [
    path('api/', include(router.urls)),
]
