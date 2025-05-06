from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class FredUser(AbstractUser):
    username = models.CharField(
        _("phone number"),
        max_length=50,
        unique=True,
        validators=[
            RegexValidator(
                regex=r"^9\d{9}$",
                message=_("Please enter the phone in the format *********9"),
            )
        ],
    )
    modified_date = models.DateTimeField(_("modified date"), auto_now=True)
    date_joined = models.DateTimeField(_("date joined"), auto_now_add=True)

    def __str__(self):
        return f"{self.username}"

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
