# Generated by Django 2.2.1 on 2019-06-27 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0024_auto_20190627_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='we_pred',
            name='img',
            field=models.ImageField(blank=True, upload_to='img/', verbose_name='Картинка'),
        ),
    ]
