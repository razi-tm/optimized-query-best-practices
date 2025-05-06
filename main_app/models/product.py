from django.db import models
from django.utils.translation import gettext_lazy as _

from main_app.models import Base


class Product(Base):
    name  = models.CharField(
        _("name"),
        max_length=200
    )
    price = models.DecimalField(
        _("price"),
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return f"Product {self.id}"

    class Meta:
        verbose_name = _("product")
        verbose_name_plural = _("products")
