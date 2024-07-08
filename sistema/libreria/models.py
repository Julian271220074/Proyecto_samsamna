from typing import Any
from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name='Nombre')
    def __str__(self):
        return self.nombre

class libro(models.Model):
    id=models.AutoField(primary_key=True)
    titulo=models.CharField(max_length=100, verbose_name='Titulo')
    imagen= models.ImageField(upload_to='imagenes/', verbose_name='Imagen', null=True)
    descripcion= models.TextField(verbose_name='Descripcion', null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='libros',verbose_name='Categoria', null=True)
    
    def __str__(self):
        fila ="Titulo: " + self.titulo + " -  Descripcion: " + self.descripcion
        return fila
    
    def delete(self, using= None, keep_parents= False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
    


