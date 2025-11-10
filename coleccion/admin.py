from django.contrib import admin
from .models import Plataforma, Genero, Videojuego

# Registramos los modelos para que aparezcan en el panel / admin
admin.site.register(Plataforma)
admin.site.register(Genero)
admin.site.register(Videojuego)