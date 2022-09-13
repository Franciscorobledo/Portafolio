#importar el  metodo llamado path  desde url
from django.urls import path
from  .views import render_post,post_detail


app_name='blog'
#definimos 
urlpatterns= [
    path('',render_post,name='post'),
    #personlazar el post 
    path('<int:post_id>', post_detail, name='post_detail')
]
