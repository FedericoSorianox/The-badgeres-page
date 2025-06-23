from django.shortcuts import render

# Create your views here.
# tareas/views.py
from rest_framework import viewsets
from .serializers import TareaSerializer
from .models import Tarea

class TareaViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite ver o editar tareas.
    """
    queryset = Tarea.objects.all().order_by('-id')
    serializer_class = TareaSerializer