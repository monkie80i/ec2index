from django.db import models

# Create your models here.
class Project(models.Model):
	name = models.CharField(max_length=20)
	description = models.TextField(max_length=200)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	active = models.BooleanField(default=True)
