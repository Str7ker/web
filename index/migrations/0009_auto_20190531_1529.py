# Generated by Django 2.2.1 on 2019-05-31 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0008_auto_20190531_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='text',
            field=models.CharField(blank=True, max_length=700),
        ),
    ]