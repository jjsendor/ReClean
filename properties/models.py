from django.db import models

class Property(models.Model):
	address = models.CharField(max_length=200)

class Tennant(models.Model):
	responded = models.BooleanField()
