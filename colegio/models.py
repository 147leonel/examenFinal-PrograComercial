from django.db import models
from django.contrib import admin

class Alumno(models.Model):
    carne= models.CharField(max_length=9)
    nombre  =   models.CharField(max_length=50)
    apellidos =models.CharField(max_length=75)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre

class Curso(models.Model):
    nombre    = models.CharField(max_length=60)
    alumnos   = models.ManyToManyField(Alumno, through='Cursando')

    def __str__(self):
        return self.nombre

class Cursando (models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

class CursandoInLine(admin.TabularInline):
    model = Cursando
#muestra una linea extra al momento de insertar, como indicación al usuario que se pueden ingresar varios actores.
    extra = 1


class AlumnoAdmin(admin.ModelAdmin):
    inlines = (CursandoInLine,)

class CursoAdmin (admin.ModelAdmin):
    inlines = (CursandoInLine,)