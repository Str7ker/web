from django.db import models

class Contact_info(models.Model):
    title = models.CharField(verbose_name="Описание страницы", max_length=70, blank=True)
    desc = models.CharField(verbose_name="Описание сайта для поисковых систем", max_length=250, blank=True)
    keywords = models.CharField(verbose_name="Ключевые слова", max_length=500, blank=True)

    class Meta:
        verbose_name = 'Контактная информация'
        verbose_name_plural = 'Контактные информации'


class Contacts(models.Model):
    phone = models.CharField(verbose_name="Телефон", max_length=25, blank=True, default="+7 (848) 262-1770")
    email = models.CharField(verbose_name="Электронная почта", max_length=30, default="info@example.ru")
    address_fact = models.CharField(verbose_name="Адрес", max_length=250, blank=True, default="ул. Улицы дом улица")
    vk = models.CharField(verbose_name="ВКонтакте", max_length=150, blank=True, default="vk.com")
    insta = models.CharField(verbose_name="Инстаграм", max_length=150, blank=True, default="instagram.com")
    inn = models.CharField(verbose_name="ИНН", max_length=50, blank=True, default="12345")
    ogrn = models.CharField(verbose_name="ОГРН", max_length=50, blank=True, default="12345")
    kpp = models.CharField(verbose_name="КПП", max_length=50, blank=True, default="12345")
    img = models.ImageField(verbose_name="Картинка", upload_to='static/img/', blank=True, default="map-min.png")
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'