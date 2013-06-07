from django.db import models

# Create your models here.
class Place(models.Model):
	name = models.CharField(max_length=255)
	room = models.CharField(max_length=255)
	module = models.CharField(max_length=2)
	row = models.IntegerField()
	column = models.IntegerField()
	depth = models.IntegerField()
	

class Part(models.Model):
	name = models.CharField(max_length=255)
	general_type = models.CharField(max_length=255)
	specific_type = models.CharField(max_length=255)
	from_value = models.FloatField()
	to_value = models.FloatField()
	package = models.CharField(max_length=255)
	place = models.ForeignKey(Place)
	note = models.TextField()
	remaining = models.IntegerField()

	
