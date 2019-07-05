from django.db import models
from datetime import datetime

class Admin_main(models.Model):
    title1 = models.CharField(verbose_name="Главное наименование", max_length=25, blank=True)
    title2 = models.CharField(verbose_name="Наименование url", max_length=30, blank=True)
    url = models.CharField(verbose_name="Адрес", max_length=250, blank=True)
    count = models.CharField(verbose_name="Счётчик приложения", max_length=150, blank=True)
    color = models.CharField(verbose_name="Цвет иконки", max_length=50, blank=True)
    ico = models.CharField(verbose_name="Иконка", max_length=50, blank=True)
    date_add = models.DateField(verbose_name="Дата добавления", default=datetime.now(), blank=True)
    date_edit = models.DateField(verbose_name="Дата редактирования", null=True, blank=True)
    class Meta:
        verbose_name = 'Главная меню'
        verbose_name_plural = 'Главная меню'

    # def __str__(self):
    #     return "Контакт " + self.phone