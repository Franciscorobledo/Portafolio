
from django.db import models
# importar tipos de dato
from django.db.models.fields import CharField
from django.db.models.fields import URLField

# importar imagenes
from django.db.models.fields.files import ImageField


# el comand format   ( f1  y escribir format ) sirve para formatear el modelo

class Project(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length=250)
    image = ImageField(upload_to='porfolio/images/')
    url = URLField(blank=True)


# para migrar a la base de dato sql lite  se ejecuta el siguiente comando
# py  manage.py makemigrations
# ejecutarlo:  py  manage.py migrate
