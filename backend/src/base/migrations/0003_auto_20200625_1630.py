# Generated by Django 2.2.13 on 2020-06-25 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20200624_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pushes',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, help_text='Дата создания: автополе', verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='pushes',
            name='name',
            field=models.CharField(help_text='Название уведомления', max_length=255, verbose_name='Название уведомления'),
        ),
        migrations.AlterField(
            model_name='pushes',
            name='picture',
            field=models.ImageField(blank=True, help_text='Пример: https://yourapp.com/image.png', null=True, upload_to='pictures', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='pushes',
            name='sent_at',
            field=models.DateField(blank=True, help_text='Дата отправки', null=True, verbose_name='Дата отправки'),
        ),
        migrations.AlterField(
            model_name='pushes',
            name='text',
            field=models.TextField(blank=True, help_text='Введите текст уведомления', verbose_name='Текст уведомления'),
        ),
        migrations.AlterField(
            model_name='pushes',
            name='title',
            field=models.CharField(help_text='Укажите заголовок', max_length=50, verbose_name='Заголовок уведомления'),
        ),
    ]
