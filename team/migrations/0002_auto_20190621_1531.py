# Generated by Django 2.2.1 on 2019-06-21 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='img',
            field=models.ImageField(blank=True, upload_to='img/team/', verbose_name='Картинка'),
        ),
    ]