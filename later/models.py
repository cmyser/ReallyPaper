from django.db import models

# Create your models here.
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField(blank=True)
    description = models.CharField(max_length=255, default='none')
    dara = models.DateTimeField(blank=True, null=True)
    url = models.SlugField(max_length=160, unique=True)

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"slug": self.url})


    def __str__(self):
        return self.title

