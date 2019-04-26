from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.
class Introduce(models.Model):
    name = models.CharField(max_length=100, validators=[MinLengthValidator(2)])
    birthday = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=100)
    religion = models.TextField(max_length=50)
    hobby = models.TextField(max_length=100)
    like_it = models.TextField(blank=True)
