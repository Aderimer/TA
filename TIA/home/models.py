from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

# Profil
class Profil(models.Model):
    navn = models.CharField(max_length=100)
    passord = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.navn}'
    
# Bilder/Postene
class Post(models.Model):
    tittel = models.CharField(max_length=100, default='', blank=False, null=False)
    beskrivelse = models.CharField(max_length=500, default='', blank=True, null=True)
    bilde = models.ImageField(upload_to='uploads/')
    dato = models.DateTimeField(default=datetime.datetime.today)

    def __str__(self):
        return self.tittel