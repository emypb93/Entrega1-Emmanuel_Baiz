from django.db import models

# Create your models here.
class Nacionalidad(models.Model):
    id_nacionalidad = models.AutoField(primary_key = True)
    nombre_pais = models.CharField(max_length = 50)

class Autor(models.Model):
    id_autor = models.AutoField(primary_key = True) # Este campo se genera solo o se puede crear asi
    nombre = models.CharField(max_length=20, blank = False, null = False) # blank = false, null = false
    apellido = models.CharField(max_length=20, blank = False, null = False)
    nacionalidad = models.ManyToManyField(Nacionalidad)
    descripcion = models.TextField()

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key = True)
    descripcion_categoria = models.CharField(max_length = 20)


class Libro(models.Model):
    id_libro= models.AutoField(primary_key = True)
    isbn = models.IntegerField()
    titulo = models.CharField(max_length = 50)
    edicion = models.IntegerField()
    ejemplares = models.IntegerField()
    ejemplares_disponibles = models.IntegerField()
    fecha_publicacion = models.DateField()
    autor_id = models.ManyToManyField(Autor)
    id_categoria = models.ManyToManyField(Categoria)


    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['titulo']

    def __str__(self):
        return self.titulo