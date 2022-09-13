from django.contrib import admin

#añadiendo el modelo admin   para controlarlo con el administrador 


from .models import Project


admin.site.register(Project)
#-----------------------------------------------