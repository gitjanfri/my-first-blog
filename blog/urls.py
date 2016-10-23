from django.conf.urls import url
from . import views

#Stiamo solo importando metodi che appartengono a Django e tutte le nostre views dalla nostra app blog 
#(non abbiamo ancora nulla all'interno, ma rimedieremo a questo in un minuto!)

#Dopo di che, possiamo aggiungere il nostro primo modello di URL:

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
