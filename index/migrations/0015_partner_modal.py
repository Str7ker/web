# Generated by Django 2.2.1 on 2019-06-11 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0014_auto_20190611_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='modal',
            field=models.CharField(blank=True, max_length=150, verbose_name='Модальное окно'),
        ),
    ]
