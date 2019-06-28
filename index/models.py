from django.db import models


class Contact(models.Model):
    phone = models.CharField(verbose_name="Телефон", max_length=25, blank=True)
    email = models.CharField(verbose_name="Электронная почта", max_length=30, blank=True)
    address_fact = models.CharField(verbose_name="Адрес", max_length=250, blank=True)
    vk = models.CharField(verbose_name="ВКонтакте", max_length=150, blank=True)
    insta = models.CharField(verbose_name="Инстаграм", max_length=150, blank=True)

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return "Контакт " + self.phone

class Romb(models.Model):
    name_romb = models.CharField(verbose_name="Наименование ромба", max_length=150, blank=True)
    ico = models.CharField(verbose_name="Иконка", max_length=25, blank=True)
    text = models.CharField(verbose_name="Текст", max_length=50, blank=True)
    numbers = models.CharField(verbose_name="Цифры", max_length=10, blank=True)

    class Meta:
        verbose_name = 'Ромб'
        verbose_name_plural = 'Ромбы'

class Car(models.Model):
    name_cars = models.CharField(verbose_name="Наименование грузоперевозки", max_length=150, blank=True)
    img = models.ImageField(verbose_name="Картинка", upload_to='img/', blank=True)
    name = models.CharField(verbose_name="Наименование", max_length=25, blank=True)
    text = models.CharField(verbose_name="Текст", max_length=250, blank=True)

    class Meta:
        verbose_name = 'Грузоперевозки'
        verbose_name_plural = 'Грузоперевозки'

class Work(models.Model):
    name_work = models.CharField(verbose_name="Наименование работы", max_length=150, blank=True)
    img = models.ImageField(verbose_name="Картинка", upload_to='static/img/work/', blank=True)
    name = models.CharField(verbose_name="Наименование", max_length=25, blank=True)
    text = models.CharField(verbose_name="Текст", max_length=700, blank=True)

    class Meta:
        verbose_name = 'Как мы работаем'
        verbose_name_plural = 'Как мы работаем'

class Partner(models.Model):
    name_part = models.CharField(verbose_name="Наименование партнёра", max_length=150, blank=True)
    img = models.ImageField(verbose_name="Логотип", upload_to='static/img/partners/', blank=True)

    class Meta:
        verbose_name = 'Партнёр'
        verbose_name_plural = 'Партнёры'

class AllPartner(models.Model):
    name_part = models.CharField(verbose_name="Наименование партнёра", max_length=150, blank=True)
    img = models.ImageField(verbose_name="Логотип", upload_to='img/partners/', blank=True)
    text = models.CharField(verbose_name="Описание партнёра", max_length=650, blank=True)
    number = models.CharField(verbose_name="Номер телефона", max_length=50, blank=True)
    email = models.CharField(verbose_name="Электронная почта", max_length=50, blank=True)

    class Meta:
        verbose_name = 'Все партнёры'
        verbose_name_plural = 'Все партнёры'
class Team(models.Model):
    img = models.ImageField(verbose_name="Картинка", upload_to='static/img/team/', blank=True)
    name = models.CharField(verbose_name="Имя и фамилия", max_length=150, blank=True)
    position = models.CharField(verbose_name="Должность", max_length=50, blank=True)
    phone = models.CharField(verbose_name="Телефон", max_length=20, blank=True)
    mail = models.CharField(verbose_name="Электронная почта", max_length=50, blank=True)
    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'

class We_pred(models.Model):
    name_pred = models.CharField(verbose_name="Наименование", max_length=150, blank=True)
    img = models.ImageField(verbose_name="Картинка", upload_to='img/pred/', blank=True)
    text = models.CharField(verbose_name="Текст", max_length=150, blank=True)

    class Meta:
        verbose_name = 'Мы представляем'
        verbose_name_plural = 'Мы представляем'

class Description(models.Model):
    desc = models.CharField(verbose_name="Описание", max_length=500, blank=True)

    class Meta:
        verbose_name = 'Описание сайта'
        verbose_name_plural = 'Описания сайта'

class Keywords(models.Model):
    keyw = models.CharField(verbose_name="Ключевые слова", max_length=500, blank=True)

    class Meta:
        verbose_name = 'Ключевые слова сайта'
        verbose_name_plural = 'Ключевые слова сайта'

class Email_order(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=500, blank=True)
    email = models.CharField(verbose_name="Электронная почта", max_length=500, blank=True)
    phone = models.CharField(verbose_name="Телефон", max_length=500, blank=True)

    class Meta:
        verbose_name = 'Завка'
        verbose_name_plural = 'Заявки'

class Logo(models.Model):
    small_logo = models.ImageField(verbose_name="Маленькое лого", upload_to='img/', blank=True)
    logo = models.ImageField(verbose_name="Большое лого", upload_to='img/', blank=True)
    background = models.ImageField(verbose_name="Задний фон картинка", upload_to='img/', blank=True)

    class Meta:
        verbose_name = 'Логотип'
        verbose_name_plural = 'Логотип'

class Order(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=50, blank=True)
    phone = models.CharField(verbose_name="Телефон", max_length=20, blank=True)
    email = models.CharField(verbose_name="Электронная почта", max_length=100, blank=True)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'