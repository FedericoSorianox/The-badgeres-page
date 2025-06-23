from django.db import models

# Create your models here.
# tareas/models.py
from django.db import models

class Tarea(models.Model):
    titulo = models.CharField(max_length=200)
    completada = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo