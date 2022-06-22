from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    tytul = models.CharField(
        max_length=40,
    )
    autor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    zawartosc = models.TextField(
        default="Text there",
    )
