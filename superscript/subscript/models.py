from django.db import models

# Create your models here.

class TextAlgorithm(models.Model):
	querry = models.CharField(max_length=300, null=True)

