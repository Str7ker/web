# Generated by Django 2.2.1 on 2019-06-25 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_auto_20190617_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='ico',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Иконка меню'),
        ),
    ]
