from django.db import models

# Create your models here.

class TempVolModel(models.Model):
	temp_intake = models.IntegerField()

	def __str__(self):
		return "ЦВУ "