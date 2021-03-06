# Generated by Django 2.2.1 on 2019-07-03 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_auto_20190628_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='address_fact',
            field=models.CharField(blank=True, default='ул. Улицы дом улица', max_length=250, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='email',
            field=models.CharField(default='info@example.ru', max_length=30, verbose_name='Электронная почта'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='img',
            field=models.ImageField(blank=True, default='map-min.png', upload_to='static/img/', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='inn',
            field=models.CharField(blank=True, default='12345', max_length=50, verbose_name='ИНН'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='insta',
            field=models.CharField(blank=True, default='instagram.com', max_length=150, verbose_name='Инстаграм'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='kpp',
            field=models.CharField(blank=True, default='12345', max_length=50, verbose_name='КПП'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='ogrn',
            field=models.CharField(blank=True, default='12345', max_length=50, verbose_name='ОГРН'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='phone',
            field=models.CharField(blank=True, default='+7 (848) 262-1770', max_length=25, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='vk',
            field=models.CharField(blank=True, default='vk.com', max_length=150, verbose_name='ВКонтакте'),
        ),
    ]
