from django.contrib import admin
from django.urls import path, include
from Datos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('', include('Datos.urls')),

    path('list/', views.list),
    path('pdf/<int:id>', views.pdf),
    path('pdf/', views.pdf),

    path('predecir_cancer/', views.predecir_cancer),
    path('predict_cancer/', views.predict_cancer, name='predict_cancer'),
]