
from django.http import HttpResponse
from django.shortcuts import render
from .models import RemisionCaso
from django.template.loader import get_template
from xhtml2pdf import pisa

# Create your views here.

def index (request):
    return render(request, 'index.html')

def pdf(request, id):
    if id:
        formulario = RemisionCaso.objects.get(id=id)
    else:
        formulario = RemisionCaso.objects.all().last() # Obtener el último formulario en caso de crearse nuevo
    # Crear el contexto para la plantilla
    context = {'formulario': formulario}

    # Cargar la plantilla HTML
    template = get_template("template.html")
    html = template.render(context)

    # Crear un objeto HttpResponse con el tipo de contenido PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="documento.pdf"'

    # Generar el PDF
    pisa_status = pisa.CreatePDF(html, dest=response)

    # Verificar si hubo errores al crear el PDF
    if pisa_status.err:
        return HttpResponse('Error al generar el PDF')
    return response
