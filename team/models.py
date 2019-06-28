from django.db import models

class Teams(models.Model):
    img = models.ImageField(verbose_name="Картинка", upload_to='img/team/', blank=True)
    name = models.CharField(verbose_name="Имя и фамилия", max_length=150, blank=True)
    position = models.CharField(verbose_name="Должность", max_length=50, blank=True)
    phone = models.CharField(verbose_name="Телефон", max_length=20, blank=True)
    mail = models.CharField(verbose_name="Электронная почта", max_length=50, blank=True)
    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'

class TextTeam(models.Model):
    text = models.CharField(verbose_name="Текст о сотрудниках", max_length=1000, blank=True)

    class Meta:
        verbose_name = 'Текст о сотрудниках'
        verbose_name_plural = 'Текст о сотрудниках'
