from django.db.models.deletion import CASCADE
from django.db import models
from django.urls import reverse

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='author')
    title = models.CharField(max_length=50, verbose_name='title')
    text = models.TextField(verbose_name='main text')


    def __str__(self):
        return self.title


    def get_absolute_url(self):             
        return reverse("detail_post", kwargs={"pk": str(self.pk)})
    