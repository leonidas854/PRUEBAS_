from django.db import models

# Create your models here.

class Frase(models.Model):
    autor = models.CharField(max_length=50)
    texto = models.TextField()