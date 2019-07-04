# Generated by Django 2.2.1 on 2019-07-04 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin_main',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1', models.CharField(blank=True, max_length=25, verbose_name='Главное наименование')),
                ('title2', models.CharField(blank=True, max_length=30, verbose_name='Наименование url')),
                ('url', models.CharField(blank=True, max_length=250, verbose_name='Адрес')),
                ('count', models.CharField(blank=True, max_length=150, verbose_name='Счётчик приложения')),
            ],
            options={
                'verbose_name': 'Главная меню',
                'verbose_name_plural': 'Главная меню',
            },
        ),
    ]
