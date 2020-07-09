from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from orders_api.models import Organization

class Status(models.Model):
	name = models.CharField(max_length=100)
	key = models.CharField(max_length=1)

class Role(models.Model):
	name = models.CharField(max_length=100)
	key = models.CharField(max_length=1)

class User(AbstractUser):
	role = models.ForeignKey(Role, on_delete=models.PROTECT, default=3)

class UserOrganization(models.Model):
	user = models.ForeignKey(Role, on_delete=models.PROTECT , related_name="userorganization")
	organization = models.ForeignKey(Organization, on_delete=models.PROTECT , related_name="userorganization")
