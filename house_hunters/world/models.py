from django.contrib.gis.db import models

# Create your models here.

class HousingCoordinates(models.Model):
	name = models.CharField(max_length=50)
	latitude = models.FloatField()
	longitude = models.FloatField()


	# Returns string version of model
	def __str__(self):
		return self.name
