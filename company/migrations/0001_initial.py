# Generated by Django 2.2.1 on 2019-06-18 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_romb', models.CharField(blank=True, max_length=150, verbose_name='Наименование ромба')),
                ('ico', models.CharField(blank=True, max_length=25, verbose_name='Иконка')),
                ('text', models.CharField(blank=True, max_length=50, verbose_name='Текст')),
                ('numbers', models.CharField(blank=True, max_length=10, verbose_name='Цифры')),
            ],
            options={
                'verbose_name': 'Компания',
                'verbose_name_plural': 'Компании',
            },
        ),
    ]