from django.db import models
from django.utils.translation import ugettext_lazy as _


class Options(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name=_('Название опции')
    )

    value = models.BooleanField(
        default=True,
        verbose_name=_('Значение')
    )
