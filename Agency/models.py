from django.db import models

class Contest1(models.Model):
    email = models.EmailField()
    name = models.CharField(default="", max_length=128)
    age = models.IntegerField()
	
class Contest2(models.Model):
	first_name = models.CharField(default="", max_length=128)
	last_name = models.CharField(default="", max_length=128)
	age = models.IntegerField()
	email = models.EmailField()
	zip = models.IntegerField()
	phone = models.IntegerField()
	
class Friend(models.Model):
	frist_name = models.CharField(default="", max_length=128)
	age = models.IntegerField()
	user_email = models.EmailField()
	friend_name1 = models.CharField(default="", max_length=128)
	friend1_email = models.EmailField()
	friend_name2 = models.CharField(default="", max_length=128)
	friend2_email = models.EmailField()
	friend_name3 = models.CharField(default="", max_length=128)
	friend3_email = models.EmailField()
	
	