from statistics import mode
from django.db import models

class Post(models.Model):
    main_text = models.TextField(verbose_name="Main text")

    def __str__(self):
        return self.main_text[:10]
