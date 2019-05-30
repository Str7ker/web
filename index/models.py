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
