from ast import Delete
from asyncio.windows_events import NULL
from cProfile import label
from distutils.command.upload import upload
from email.policy import default
from statistics import mode
from turtle import title
from urllib import request
from venv import create
from django.db import models
from django.contrib.auth.models import AbstractUser
from pkg_resources import require

class CustomUser(AbstractUser):
    user_image = models.ImageField(upload_to='media', verbose_name="Фото профиля")
    money = models.DecimalField(decimal_places=2, max_digits=10, default=100, verbose_name="Накопления")


class Type(models.Model):
    slug = models.CharField(max_length=50, unique=True, verbose_name="URL измерения")
    title = models.CharField(max_length=25, unique=True, verbose_name="Название")

    def __str__(self):
        return self.title
    
class Figure(models.Model):
    slug = models.CharField(max_length=50, unique=True, verbose_name="URL figure")
    image = models.ImageField(upload_to="media", verbose_name="Image")
    title = models.CharField(max_length=25, verbose_name="Title")
    text = models.TextField(verbose_name="Text")
    cost = models.DecimalField(decimal_places=2, max_digits=10, default=0, verbose_name="Cost")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Владелец", default=NULL)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name="Type", default=NULL)
    likes = models.IntegerField(verbose_name="likes", default=0)

    def __str__(self):
        return self.title

class FigureBlacklist(models.Model):
    figure = models.ForeignKey(Figure, on_delete=models.CASCADE, verbose_name="Figure")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="User")

class FigureLikeManager(models.Manager):
    def create_like(self, figure, user):
        like = self.create(figure=figure, user=user)
        figure.likes += 1
        figure.save()
        return like

    def delete_like(self, figure, user):
        like = self.get(figure=figure, user=user)
        figure.likes -= 1
        figure.save()
        like.delete()


class FigureLike(models.Model):
    figure = models.ForeignKey(Figure, on_delete=models.CASCADE, verbose_name="Figure")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="User")
    objects = FigureLikeManager()
