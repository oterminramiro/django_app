from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class Status(models.Model):
	name = models.CharField(max_length=100)
	key = models.CharField(max_length=1)

class Role(models.Model):
	name = models.CharField(max_length=100)
	key = models.CharField(max_length=1)

class User(AbstractUser):
	role = models.ForeignKey(Role, on_delete=models.PROTECT, default=3)
