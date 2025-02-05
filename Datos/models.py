from datetime import timezone
from django.db import models
from django.forms import ValidationError

# Create your models here.

class RemisionCaso(models.Model):
    unidad = models.CharField(max_length=100)
    no_historia_clinica_individual = models.CharField(max_length=50)
    no_historia_clinica_hospital_base = models.CharField(max_length=50)
    consultorio_medico_familia = models.CharField(max_length=50)
    
    referido_a = models.CharField(max_length=100)
    fecha_turno_programado = models.DateField()
    hora_turno_programado = models.TimeField()
    
    sexo = models.CharField(max_length=10, choices=[('Femenino', 'Femenino'), ('Masculino', 'Masculino')])
    edad = models.PositiveIntegerField()
    color_piel = models.CharField(max_length=10, choices=[('Blanca', 'Blanca'), ('Negra', 'Negra'), ('Mestiza', 'Mestiza')])
    nacimiento = models.CharField(default="null", max_length=100)
    fecha_nacimiento = models.DateField()
    
    nombre = models.CharField(max_length=100)
    primer_apellido = models.CharField(max_length=100)
    segundo_apellido = models.CharField(max_length=100)

    residencia_habitual = models.CharField(max_length=255)
    apartamento = models.CharField(max_length=255)
    no_o_km = models.CharField(max_length=50)
    edificio = models.CharField(max_length=50)
    direccion_entre_calles = models.CharField(max_length=100)
    localidad = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    nombre_padre = models.CharField(max_length=100)
    nombre_madre = models.CharField(max_length=100)
    estado_vital_padre = models.CharField(max_length=10, choices=[('Vivo', 'Vivo'), ('Muerto', 'Muerto')])
    estado_vital_madre = models.CharField(max_length=10, choices=[('Vivo', 'Vivo'), ('Muerto', 'Muerto')])
    
    referido_a_especialista_de = models.CharField(max_length=100)
    antecedentes_interes = models.TextField()
    resumen_sindromico = models.TextField()
    resumen_examen_fisico = models.TextField()
    tratamiento = models.TextField()
    evolucion = models.TextField()
    impresion_diagnostica = models.TextField()
    otros_diagnosticos = models.TextField(blank=True, null=True)

    nombre_medico = models.CharField(max_length=100)
    firma_medico = models.ImageField(null=True, blank=True, upload_to='firma_medico/')
    fecha = models.DateField()
    
   
    def clean(self):
        # Validación personalizada para la edad
        if self.edad < 0 or self.edad > 120:
            raise ValidationError(('Edad debe estar entre 0 y 120 años'))

        # Validación personalizada para la fecha de nacimiento
        if self.fecha_nacimiento > self.fecha_turno_programado:
            raise ValidationError(('La fecha de nacimiento no puede ser posterior a la fecha del turno programado'))

        # Validación personalizada para el nombre
        if not self.nombre.isalpha():
            raise ValidationError(('El nombre solo debe contener letras'))

        # Validación personalizada para el primer apellido
        if not self.primer_apellido.isalpha():
            raise ValidationError(('El primer apellido solo debe contener letras'))

        # Validación personalizada para el segundo apellido
        if not self.segundo_apellido.isalpha():
            raise ValidationError(('El segundo apellido solo debe contener letras'))

    def save(self, *args, **kwargs):
        # Llamar al método clean() para ejecutar las validaciones personalizadas
        self.clean()
        super(RemisionCaso, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.nombre} {self.primer_apellido} {self.segundo_apellido}'