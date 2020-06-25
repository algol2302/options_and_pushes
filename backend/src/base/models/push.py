from django.db import models
from django.utils.translation import ugettext_lazy as _


class Pushes(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name=_('Заголовок уведомления'),
        help_text=_('Укажите заголовок')
    )

    text = models.TextField(
        blank=True,
        verbose_name=_('Текст уведомления'),
        help_text=_('Введите текст уведомления')
    )

    picture = models.ImageField(
        verbose_name=_('Картинка'),
        upload_to='pictures',
        blank=True,
        null=True,
        help_text=_('Пример: https://yourapp.com/image.png')
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Дата создания'),
        help_text=_('Дата создания: автополе')
    )

    sent_at = models.DateField(
        null=True,
        blank=True,
        verbose_name=_('Дата отправки'),
        help_text=_('DD/MM/YY')
    )

    name = models.CharField(
        max_length=255,
        verbose_name=_('Название уведомления'),
        help_text=_('Название уведомления'),
    )

    amount = models.PositiveSmallIntegerField(
        default=0,
        verbose_name=_('Количество отправленных пушей')
    )
