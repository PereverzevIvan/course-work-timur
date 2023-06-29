import random
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from os import sep
from django.utils.safestring import mark_safe

def photo_path():
        chars= 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
        file_name = ''.join((random.choice(chars)) for x in range(30))
        return file_name

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    text = models.TextField(verbose_name='Содержание')
    image = models.ImageField(upload_to=f'images/articles/%Y/%m/%d/{photo_path()}.jpg', verbose_name='Изображение')
    created_at = models.DateField(null=True, auto_now_add=True, verbose_name='Дата написания')

    class Meta:
        verbose_name = "Статью"
        verbose_name_plural = "Статьи"


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Новость')
    text = models.TextField(verbose_name='Содержание')
    created_at = models.DateField(null=True, auto_now_add=True, verbose_name='Дата написания')

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии к статьям"


class Advertisement(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    image = models.ImageField(upload_to=f'images/advertisements/%Y/%m/%d/{photo_path()}.jpg', verbose_name='Изображение')
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    text = models.TextField(verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена')
    is_close = models.BooleanField(default=False, verbose_name='Закрыто')

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"


class Car(models.Model):
    mark = models.CharField(max_length=200, verbose_name="Марка")
    model = models.CharField(max_length=200, verbose_name="Модель")
    year = models.IntegerField(verbose_name='Год выпуска')
    color = models.CharField(max_length=200, verbose_name="Цвет")
    vin_number = models.CharField(max_length=200, verbose_name="VIN номер")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец')
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE, verbose_name='Объявление')

    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"


class Rating(models.Model):
     evaluating = models.ForeignKey(User, on_delete=models.CASCADE, related_name='evaluating', verbose_name='Оценивающий')
     evaluated = models.ForeignKey(User, on_delete=models.CASCADE, related_name='evaluated', verbose_name='Оцениваемый')
     value = models.IntegerField(verbose_name='Оценка')

     class Meta:
        verbose_name = "Оценку"
        verbose_name_plural = "Оценки авторов объявлений"


class Сommunication(models.Model):
     sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender', verbose_name='Отправитель')
     recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipient', verbose_name='Получатель')
     text = models.TextField(verbose_name='Содержание')
     created_at = models.DateField(null=True, auto_now_add=True, verbose_name='Дата написания')

     class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Общение"
