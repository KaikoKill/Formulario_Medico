from django.http import HttpResponse
from django.shortcuts import render
from .models import RemisionCaso
from django.template.loader import get_template
from xhtml2pdf import pisa
import joblib

# Create your views here.

def index (request):
    return render(request, 'index.html')

def list(request):
    formularios = RemisionCaso.objects.all()
    return render(request, 'list.html', {'formularios': formularios})

def predecir_cancer(request):
    return render(request, 'predecir_cancer.html')

def pdf(request, id=None):
    if id:
        formulario = RemisionCaso.objects.all().get(id=id)
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

def predict_cancer(request):
    if request.method == 'POST':
        # Obtener datos del formulario
        espesor_grupo = float(request.POST.get('espesor_grupo'))
        uniformidad_tamano_celda = float(request.POST.get('uniformidad_tamano_celda'))
        uniformidad_forma_celda = float(request.POST.get('uniformidad_forma_celda'))
        adherencia_marginal = float(request.POST.get('adherencia_marginal'))
        tamano_celula_epitelial = float(request.POST.get('tamano_celula_epitelial'))
        nucleos_desnudos = float(request.POST.get('nucleos_desnudos'))
        cromatina_blanda = float(request.POST.get('cromatina_blanda'))
        nucleolos_normales = float(request.POST.get('nucleolos_normales'))
        mitosis = float(request.POST.get('mitosis'))
        
        # Cargar modelo y hacer predicción
        datos = [[
            espesor_grupo,
            uniformidad_tamano_celda,
            uniformidad_forma_celda,
            adherencia_marginal,
            tamano_celula_epitelial,
            nucleos_desnudos,
            cromatina_blanda,
            nucleolos_normales,
            mitosis
        ]]
        
        modelo = joblib.load('Modelo IA/random_forest_model.pkl')
        clase_predicha = modelo.predict(datos)[0]
        
        # Mapear a nombre de clase
        clases = ['Benigno', 'Maligno']
        prediccion = clases[clase_predicha]
    
        return render(request, 'predecir_cancer.html', {'prediccion': prediccion})