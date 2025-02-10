from django.contrib import admin
from django.urls import path, include
from Datos import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name = 'main'),
    path('', include('Datos.urls')),
    
    path('agg/', views.Agregar_Paciente, name='agg'),
    path('list/', views.list.as_view(template_name = 'list.html'), name='list'),
    path('pdf/<int:id>', views.pdf),
    path('pdf/', views.pdf),
   # path('predecir_cancer/', views.predecir_cancer, name='predecir_cancer'),
   # path('predict_cancer/', views.predict_cancer, name='predict_cancer'),
]
