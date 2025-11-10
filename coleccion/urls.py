from django.urls import path
#Importamos todas las vistas que hemos creado en views.py
from .views import (
    VideojuegoListView,
    VideojuegoDetailView,
    VideojuegoCreateView,
    VideojuegoUpdateView,
    VideojuegoDeleteView,

    PlataformaListView,
    PlataformaCreateView,
    PlatafromaUpdateView,
    PlataformaDeleteView,
    GeneroListView,
    GeneroCreateView,
    GeneroUpdateView,
    GeneroDeleteView,
)

urlpatterns = [
    # URLs de Videojuego
    #READ (List)
    path('', VideojuegoListView.as_view(), name='lista_videojuegos'),

    #READ (Detail)
    #Usamos <int:pk> (Primary Key) para identificar el videojuego - Like findById(id)
    path('<int:pk>/', VideojuegoDetailView.as_view(), name='videojuego_detalle'),

    #CREATE
    path('nuevo/', VideojuegoCreateView.as_view(), name='videojuego_nuevo'),

    #UPDATE
    path('<int:pk>/editar/', VideojuegoUpdateView.as_view(), name='videojuego_editar'),

    #DELETE
    path('<int:pk>/borrar/', VideojuegoDeleteView.as_view(), name='videojuego_borrar'),

    # URLs de Plataforma
    # Las agrupamos debajo de 'plataformas/'
    # READ (List)
    path('plataformas/', PlataformaListView.as_view(), name='lista_plataformas'),
    #CREATE
    path('plataformas/nueva/', PlataformaCreateView.as_view(), name='plataforma_nueva'),

    #UPDATE
    path('plataformas/<int:pk>/editar', PlatafromaUpdateView.as_view(), name='plataforma_editar'),

    #DELETE
    path('plataformas/<int:pk>/borrar', PlataformaDeleteView.as_view(), name='plataforma_borrar'),
    

    # URLs de Genero
    # Los agrupamos debajo de 'generos/'

    # READ (List)
    path('generos/', GeneroListView.as_view(), name='lista_generos'),

    # CREATE
    path('generos/nuevo/', GeneroCreateView.as_view(), name='genero_nuevo'),

    #UPDATE
    path('generos/<int:pk>/editar/', GeneroUpdateView.as_view(), name='genero_editar'),

    #DELETE
    path('generos/<int:pk>/borrar/', GeneroDeleteView.as_view(), name='genero_borrar'),
]