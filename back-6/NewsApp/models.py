from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Article(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    
    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    text = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    
    def get_absolute_url(self):
        return reverse('home')
    