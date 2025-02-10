from venv import logger
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from .models import RemisionCaso
from django.template.loader import get_template
from xhtml2pdf import pisa
import os
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
class list(generic.ListView):
    model = RemisionCaso
    paginate_by = 5
    context_object_name = 'formularios'

def main(request):
    return render(request, 'main.html')

def Agregar_Paciente (request):
    return render(request, 'agg.html')

def predecir_cancer(request):
    return render(request, 'predecir_cancer.html')

def pdf(request, id=None):
    if id:
        formulario = RemisionCaso.objects.all().get(id=id)
    else:
        formulario = RemisionCaso.objects.all().last()  # Obtener el último formulario en caso de crearse nuevo

    # Convertir la URL de la imagen a una ruta absoluta del sistema de archivos
    if formulario.firma_medico: 
        imagen_path = os.path.join(settings.MEDIA_ROOT, formulario.firma_medico.name)
    else:
        imagen_path = None

    # Crear el contexto para la plantilla
    context = {
        'formulario': formulario,
        'imagen_path': imagen_path,  # Pasar la ruta absoluta de la imagen a la plantilla
    }

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
@csrf_exempt
def predict_cancer(request):
    if request.method == 'POST':
        try:
            # Obtener datos del formulario
            espesor_grupo = int(request.POST.get('espesor_grupo'))
            uniformidad_tamano_celda = int(request.POST.get('uniformidad_tamano_celda'))
            uniformidad_forma_celda = int(request.POST.get('uniformidad_forma_celda'))
            adherencia_marginal = int(request.POST.get('adherencia_marginal'))
            tamano_celula_epitelial = int(request.POST.get('tamano_celula_epitelial'))
            nucleos_desnudos = int(request.POST.get('nucleos_desnudos'))
            cromatina_blanda = int(request.POST.get('cromatina_blanda'))
            nucleolos_normales = int(request.POST.get('nucleolos_normales'))
            mitosis = int(request.POST.get('mitosis'))

            # Verificar que todos los valores sean válidos
            if None in [espesor_grupo, uniformidad_tamano_celda, uniformidad_forma_celda, adherencia_marginal, tamano_celula_epitelial, nucleos_desnudos, cromatina_blanda, nucleolos_normales, mitosis]:
                return render(request, 'predecir_cancer.html', {'error': 'Todos los campos deben ser números válidos.'})

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

            modelo_path = os.path.join(settings.BASE_DIR, 'Modelo IA', 'random_forest_model.pkl')
            modelo = joblib.load(modelo_path)
            clase_predicha = modelo.predict(datos)[0]

            # Mapear a nombre de clase
            clases = ['Benigno', 'Maligno']
            prediccion = clases[clase_predicha]

            return render(request, 'predecir_cancer.html', {'prediccion': prediccion})

        except Exception as e:
            logger.error(f"Error al predecir el cáncer: {e}")
            return render(request, 'predecir_cancer.html', {'error': 'Por motivos de sobrecarga, el modelo de aprendizaje automático no esta disponible.'},status=500)

    return render(request, 'predecir_cancer.html')