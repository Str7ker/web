# Generated by Django 2.2.1 on 2019-07-05 09:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0006_auto_20190705_1327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teams',
            name='log',
        ),
        migrations.AddField(
            model_name='teams',
            name='date_add',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 7, 5, 13, 30, 32, 469655), verbose_name='Дата добавления'),
        ),
        migrations.AddField(
            model_name='teams',
            name='date_del',
            field=models.DateField(blank=True, null=True, verbose_name='Дата удаления'),
        ),
        migrations.AddField(
            model_name='teams',
            name='date_edit',
            field=models.DateField(blank=True, null=True, verbose_name='Дата редактирования'),
        ),
        migrations.AlterField(
            model_name='teamslog',
            name='date_add',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 7, 5, 13, 30, 32, 468654), verbose_name='Дата добавления'),
        ),
    ]
