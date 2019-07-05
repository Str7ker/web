# Generated by Django 2.2.1 on 2019-07-05 09:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0007_auto_20190705_1330'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TeamsLog',
        ),
        migrations.RemoveField(
            model_name='teams',
            name='date_del',
        ),
        migrations.AlterField(
            model_name='teams',
            name='date_add',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 7, 5, 13, 33, 53, 639877), verbose_name='Дата добавления'),
        ),
    ]
