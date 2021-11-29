from django.shortcuts import render
from django.contrib import messages
from .forms import CursoForm
from colegio.models import Curso, Cursando
# Create your views here.

def curso_nuevo(request):
    if request.method == "POST":
        formulario = CursoForm(request.POST)
        if formulario.is_valid():
            curso = Curso.objects.create(nombre=formulario.cleaned_data['nombre'])
            for alumno_id in request.POST.getlist('alumnos'):
                cursando = Cursando(alumno_id=alumno_id, alumno_id = curso.id)
                cursando.save()
            messages.add_message(request, messages.SUCCESS, 'Curso guardado exitosamente')
    else:
        formulario = CursoForm()
    return render(request, 'curso/curso_editar.html', {'formulario': formulario})