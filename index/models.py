from django.db import models


class Contact(models.Model):
    phone = models.CharField(max_length=25, blank=True)
    email = models.CharField(max_length=30, blank=True)
    address_fact = models.CharField(max_length=250, blank=True)
    vk = models.CharField(max_length=150, blank=True)
    insta = models.CharField(max_length=150, blank=True)

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'

class Romb(models.Model):
    name_romb = models.CharField(max_length=150, blank=True)
    ico = models.CharField(max_length=25, blank=True)
    text = models.CharField(max_length=50, blank=True)
    numbers = models.CharField(max_length=10, blank=True)

    class Meta:
        verbose_name = 'Ромб'
        verbose_name_plural = 'Ромбы'

class Car(models.Model):
    name_cars = models.CharField(max_length=150, blank=True)
    img = models.CharField(max_length=150, blank=True)
    name = models.CharField(max_length=25, blank=True)
    text = models.CharField(max_length=250, blank=True)

    class Meta:
        verbose_name = 'Грузоперевозки'
        verbose_name_plural = 'Грузоперевозки'

class Work(models.Model):
    name_work = models.CharField(max_length=150, blank=True)
    img = models.CharField(max_length=150, blank=True)
    name = models.CharField(max_length=25, blank=True)
    text = models.CharField(max_length=700, blank=True)

    class Meta:
        verbose_name = 'Как мы работаем'
        verbose_name_plural = 'Как мы работаем'

class Partner(models.Model):
    name_part = models.CharField(max_length=150, blank=True)
    img = models.CharField(max_length=150, blank=True)

    class Meta:
        verbose_name = 'Партнёр'
        verbose_name_plural = 'Партнёры'

class We_pred(models.Model):
    name_pred = models.CharField(max_length=150, blank=True)
    img = models.CharField(max_length=150, blank=True)
    text = models.CharField(max_length=150, blank=True)

    class Meta:
        verbose_name = 'Мы представляем'
        verbose_name_plural = 'Мы представляем'

class Description(models.Model):
    desc = models.CharField(max_length=500, blank=True)

    class Meta:
        verbose_name = 'Описание сайта'
        verbose_name_plural = 'Описания сайта'

class Keywords(models.Model):
    keyw = models.CharField(max_length=500, blank=True)

    class Meta:
        verbose_name = 'Ключевые слова сайта'
        verbose_name_plural = 'Ключевые слова сайта'