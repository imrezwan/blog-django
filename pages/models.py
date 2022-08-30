from pyexpat import model
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    slug = models.CharField(max_length=255)

    def __str__(self):
        return self.title[:50]
