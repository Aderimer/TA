from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
    
# Bilder/Postene
class Post(models.Model):
    tittel = models.CharField(max_length=100, default='', blank=False, null=False)
    beskrivelse = models.CharField(max_length=500, default='', blank=True, null=True)
    bilde = models.ImageField(upload_to='uploads/')
    dato = models.DateTimeField(default=datetime.datetime.today)
    # Bilde innstillinger:
    lengde = models.IntegerField(default=500)
    høyde = models.IntegerField(default=500)
    lengde_showcase = models.IntegerField(default=1000)
    høyde_showcase = models.IntegerField(default=1000)

    def __str__(self):
        return self.tittel

# Profil til home
class Profil(models.Model):
    navn = models.CharField(max_length=100)
    tlf = models.CharField(max_length=12, default='', blank=True, null=True)
    bilde = models.ImageField(upload_to='uploads/profil/')
    kamera_navn = models.CharField(max_length=100, blank=True, null=True, default='Canon EOS 5D Mark II')
    kamera_detaljer = models.CharField(max_length=1000, default='', blank=True, null=True)

    def __str__(self):
        return self.navn
