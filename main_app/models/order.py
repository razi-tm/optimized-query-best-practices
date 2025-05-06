from django.db import models
from django.utils.translation import gettext_lazy as _

from main_app.models import Base


class Order(Base):
    user = models.ForeignKey(
        to="FredUser",
        related_name="orders",
        related_query_name='order',
        on_delete=models.CASCADE,
        verbose_name=_("user"),
    )

    def __str__(self):
        return f"Order {self.id}"

    class Meta:
        verbose_name = _("order")
        verbose_name_plural = _("orders")
