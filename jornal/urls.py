from django.urls import path
from . import views  

app_name = 'jornal'

urlpatterns = [

    path('noticia/<slug:slug>/', views.pagina_noticias, name='pagina_noticias'),

    path('adicionar-noticia/', views.add_aos_fav, name="add"),
    path('favoritos/', views.ver_favoritos, name='favoritos'), 
    path('favoritos/adicionar/<int:noticia_id>/', views.add_aos_fav, name='add_aos_fav'),
    path('favoritos/remover/<int:noticia_id>/', views.remover_dos_favoritos, name='remover_dos_favoritos'),
    path('', views.index, name='index'),
    
]