# Generated by Django 2.2.13 on 2020-06-24 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pushes',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='pictures', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='pushes',
            name='sent_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата отправки'),
        ),
    ]
