from django.db import models
from django.urls import reverse #lo usaremos más tarde

#Modelo para las Plataformas (Ej: Pc, PS5, Switch)
class Plataforma(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        #Esto es lo que veremos en el panel de admin
        return self.nombre

#Modelo para los Géneros (EJ: RPG, Shooter, Deportes, Estrategia)    
class Genero(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

#Modelo para el Videojuego    
class Videojuego(models.Model):
    titulo = models.CharField(max_length=200)

     #Relaciones ForeignKey (Un videojuego tiene UN género y UNA Plataforma)
     #(Si quisieramos MÚLTIPLES géneros usaríamos ManyToManyField)
    plataforma = models.ForeignKey(Plataforma, on_delete=models.SET_NULL, null=True, blank=True)
    genero = models.ForeignKey(Genero, on_delete=models.SET_NULL, null=True, blank=True)
    anio_salida = models.IntegerField(verbose_name="Año de Salida")

    #Campo para añadir una breve descripción
    descripcion = models.TextField(blank=True)

    #He añadido un nuevo campo para poener un imagen.
    # 'upload_to' le dice a Django que guarde la simágenes en la carpeta 
    # 'media/videojuegos/' ' null=True, blank=True' permite que sea creen videojuegos sin imagen.
    imagen = models.ImageField(upload_to='videojuegos/', null=True, blank=True)

    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        #Esta función es crucial para que Django sepa a dónde redirigir   
        #después de crear o actualizar un objeto.
        return reverse('videojuego_detalle', args=[str(self.id)])



