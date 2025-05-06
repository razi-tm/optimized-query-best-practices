from django.db import models
from django.utils.translation import gettext_lazy as _

from main_app.models import Base


class OrderItem(Base):
    order = models.ForeignKey(
        to='Order',
        related_name="order_items",
        related_query_name="order_item",
        on_delete=models.CASCADE,
        verbose_name=_("item"),
    )
    product = models.ForeignKey(
        to='Product',
        related_name="order_items",
        related_query_name="order_item",
        on_delete=models.PROTECT,
        verbose_name=_("product"),
    )
    quantity = models.PositiveIntegerField(_("quantity"), default=1)

    def __str__(self):
        return f"OrderItem {self.id}"

    class Meta:
        verbose_name = _("order item")
        verbose_name_plural = _("order items")
        indexes = [
            models.Index(fields=['order']),
            models.Index(fields=['product']),
            models.Index(fields=['order', 'product']),  # Composite index
        ]
