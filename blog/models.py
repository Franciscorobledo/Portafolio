from distutils.command.upload import upload
from email.mime import image
from turtle import update
from django.db import models
import datetime
# vmaos a crear un  modelo de dato
#f1 format document para formatear el documento

#comando para migrar el documento 
# py manage.py makemigrations
# py manage.py migrate

#_____________________________________________

class post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='blog/images')
    date = models.DateField(datetime.date.today)
