# Generated by Django 2.2.1 on 2019-07-05 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin_main',
            name='color',
            field=models.CharField(blank=True, max_length=50, verbose_name='Цвет иконки'),
        ),
        migrations.AddField(
            model_name='admin_main',
            name='ico',
            field=models.CharField(blank=True, max_length=50, verbose_name='Иконка'),
        ),
    ]
