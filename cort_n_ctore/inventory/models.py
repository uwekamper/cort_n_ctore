from django.db import models

# Create your models here.
class Place(models.Model):
	name = models.CharField(max_length=255)
	room = models.CharField(max_length=255)
	module = models.CharField(max_length=2)
	row = models.IntegerField()
	column = models.IntegerField()
	depth = models.IntegerField()
	
	def __unicode__(self):
		return u'%s, module: %s, row: %d, col: %d, depth: %d' % (self.room, self.module, 
			self.row, self.column, self.depth)
	

class Part(models.Model):
	name = models.CharField(max_length=255)
	general_type = models.CharField(max_length=255)
	specific_type = models.CharField(max_length=255)
	from_value = models.FloatField()
	to_value = models.FloatField()
	unit = models.CharField(max_length=255, default='')
	package = models.CharField(max_length=255)
	place = models.ForeignKey(Place)
	note = models.TextField()
	remaining = models.IntegerField()
	
	def __unicode__(self):
		return self.name

	
