from django.contrib import admin

#importamos el modelo definido en models 

from .models import post

admin.site.register(post)


#----------------------------------------------