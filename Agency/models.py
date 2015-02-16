from django.db import models

class Contest1(models.Model):
    email = models.EmailField()
    name = models.CharField(default="", max_length=128)
    age = models.IntegerField()
	
class Contest2(models.Model):
	first_name = models.CharField(default="", max_length=128)
	last_name = models.CharField(default="", max_length)
	age = models.IntegerField()
	email = models.EmailField()
	zip = models.IntegerField()
	phone = models.IntegerField()
	
	