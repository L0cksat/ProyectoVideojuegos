from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Videojuego, Plataforma, Genero

#--CRUD para Videojuego--

#READ (List) - (Leer todos) - Like findAll

class VideojuegoListView(ListView):
    model = Videojuego
    template_name = 'coleccion/lista_videojuegos.html' #Plantilla que usará
    context_object_name ='videojuegos' #Nombre para usar en la plantilla


#READ (Detail) - (Leer Uno) - Like findById or findOne

class VideojuegoDetailView(DetailView):
    model = Videojuego
    template_name = 'coleccion/detalle_videojuegos.html'
    context_object_name = 'videojuego'
    


#CREATE - (Crear) - Like insertOne

class VideojuegoCreateView(CreateView):
    model = Videojuego
    template_name ='coleccion/form_videojuegos.html'
    #Campos que se mostrarán en el formulario
    fields = ['titulo', 'plataforma', 'genero', 'anio_salida', 'descripcion', 'imagen']
    #No necesitamos success_url porque definimos get_aboslute_url en el modelo
    success_url = reverse_lazy('lista_videojuegos')


#UPDATE - (Actualizar) - Like updateOne

class VideojuegoUpdateView(UpdateView):
    model = Videojuego
    template_name = 'coleccion/form_videojuegos.html'
    #Usamos los mismos campos y plantilla que Create
    fields= ['titulo', 'plataforma', 'genero', 'anio_salida', 'descripcion','imagen']

#DELETE - (Borrar) - Like deleteOne

class VideojuegoDeleteView(DeleteView):
    model= Videojuego
    template_name = 'coleccion/borrar_videojuegos.html'
    # A dónde ir después de borrar con éxito
    #reverse_lazy: Es la forma segura de decirle a Django "cuando termines, ve a esta URL".
    success_url = reverse_lazy('lista_videojuegos')

#--CRUD para PLataformas --

class PlataformaListView(ListView):
    model = Plataforma
    template_name= 'coleccion/lista_plataformas.html'
    context_object_name = 'plataformas'

class PlataformaCreateView(CreateView):
    model = Plataforma
    template_name = 'coleccion/form_plataforma.html'
    fields = ['nombre']
    success_url = reverse_lazy('lista_plataformas') # Redirige a la lista

class PlatafromaUpdateView(UpdateView):
    model = Plataforma
    template_name = 'coleccion/form_plataforma.html'
    fields = ['nombre']
    success_url = reverse_lazy('lista_plataformas')

class PlataformaDeleteView(DeleteView):
    model = Plataforma
    template_name ='coleccion/borrar_plataforma.html'
    context_object_name = 'plataforma'
    success_url = reverse_lazy('lista_plataformas')

# -- CRUD para Géneros --

class GeneroListView(ListView):
    model = Genero
    template_name = 'coleccion/lista_generos.html'
    context_object_name = 'generos'

class GeneroCreateView(CreateView):
    model = Genero
    template_name = 'coleccion/form_genero.html'
    fields =['nombre']
    success_url = reverse_lazy('lista_generos')

class GeneroUpdateView(UpdateView):
    model = Genero
    template_name = 'coleccion/form_genero.html'
    fields = ['nombre']
    success_url = reverse_lazy('lista_generos')

class GeneroDeleteView(DeleteView):
    model = Genero
    template_name = 'coleccion/borrar_genero.html'
    context_object_name = 'genero'
    success_url = reverse_lazy('lista_generos')
