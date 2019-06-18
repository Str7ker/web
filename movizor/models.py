from django.db import models

class Map(models.Model):
    map_token = models.CharField(verbose_name="Токен", max_length=250, blank=True)
    title = models.CharField(verbose_name="Описание страницы", max_length=70, blank=True)
    desc = models.CharField(verbose_name="Описание сайта для поисковых систем", max_length=250, blank=True)
    keywords = models.CharField(verbose_name="Ключевые слова", max_length=500, blank=True)

    class Meta:
        verbose_name = 'Карта'
        verbose_name_plural = 'Карты'

class Map_contact(models.Model):
    ico = models.CharField(verbose_name="Иконка", max_length=25, blank=True)
    text = models.CharField(verbose_name="Текст", max_length=50, blank=True)
    info = models.CharField(verbose_name="Описание и значение", max_length=100, blank=True)

    class Meta:
        verbose_name = 'Контакт Карты'
        verbose_name_plural = 'Контакт Карт'