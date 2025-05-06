from django.db import models
from django.utils.translation import gettext_lazy as _


class Base(models.Model):
    created_date = models.DateTimeField(_("created_date"), auto_now_add=True)
    modified_date = models.DateTimeField(_("modified_date"), auto_now=True)

    class Meta:
        abstract = True
