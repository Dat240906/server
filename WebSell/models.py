from turtle import back
from django.db import models
from sympy import true

# Create your models here.



class Account(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)


class Contact(models.Model):
    title = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    content = models.CharField(max_length=1000)