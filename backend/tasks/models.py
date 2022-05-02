from venv import create
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=6)
    created_at = models.DateField(auto_now_add=True)
