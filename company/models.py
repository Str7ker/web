from django.db import models
from datetime import datetime

class Company(models.Model):
    title = models.CharField(verbose_name="Описание страницы", max_length=270, blank=True)
    small_text = models.TextField(verbose_name="Маленький текст", max_length=500, blank=True)
    big_text = models.TextField(verbose_name="Текст", max_length=1500, blank=True)
    date_add = models.DateField(verbose_name="Дата добавления", default=datetime.now(), blank=True)
    date_edit = models.DateField(verbose_name="Дата редактирования", null=True, blank=True)

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

    def __str__(self):
        return self.title

class Company_info(models.Model):
    title = models.CharField(verbose_name="Описание страницы", max_length=70, blank=True)
    desc = models.CharField(verbose_name="Описание сайта для поисковых систем", max_length=250, blank=True)
    keywords = models.CharField(verbose_name="Ключевые слова", max_length=500, blank=True)

    class Meta:
        verbose_name = 'Контактная информация'
        verbose_name_plural = 'Контактные информации'

    def __str__(self):
        return self.title

class CompanyNews(models.Model):
    title = models.CharField(verbose_name="Описание страницы", max_length=70, blank=True)
    desc = models.CharField(verbose_name="Описание сайта для поисковых систем", max_length=250, blank=True)
    keywords = models.CharField(verbose_name="Ключевые слова", max_length=500, blank=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title
