from django.db import models
from django.utils import timezone


class Status(models.Model):
    name = models.CharField(max_length=100)
    key = models.CharField(max_length=1)

class Role(models.Model):
    name = models.CharField(max_length=100)
    key = models.CharField(max_length=1)

class User(models.Model):
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    role = models.ForeignKey(Role, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
