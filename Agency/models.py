from django.db import models

class Contest1(models.Model):
    email = models.EmailField()
    name = models.CharField(default="", max_length=128)
    age = models.IntegerField()
	