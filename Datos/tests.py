from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import RemisionCaso
from datetime import date, time

# Create your tests here.
class RemisionCasoModelTest(TestCase):

    def setUp(self):
        self.remision = RemisionCaso(
            nombre="Juan",
            primer_apellido="Perez",
            segundo_apellido="Gomez",
            edad=30,
            sexo="Masculino",
            color_piel="Blanca",
            nacimiento="Ciudad",
            fecha_nacimiento=date(1990, 1, 1),
            consultorio_medico_familia="Consultorio A",
            referido_a="Especialista B",
            fecha_turno_programado=date(2023, 12, 31),
            hora_turno_programado=time(10, 0),
            residencia_habitual="Calle Falsa 123",
            apartamento="Apto 456"
        )

    def test_nombre_solo_letras(self):
        self.remision.nombre = "Juan123"
        with self.assertRaises(ValidationError):
            self.remision.clean()

    def test_primer_apellido_solo_letras(self):
        self.remision.primer_apellido = "Perez123"
        with self.assertRaises(ValidationError):
            self.remision.clean()

    def test_segundo_apellido_solo_letras(self):
        self.remision.segundo_apellido = "Gomez123"
        with self.assertRaises(ValidationError):
            self.remision.clean()

    def test_edad_valida(self):
        self.remision.edad = 150
        with self.assertRaises(ValidationError):
            self.remision.clean()

    def test_fecha_nacimiento_anterior_a_turno(self):
        self.remision.fecha_nacimiento = date(2024, 1, 1)
        with self.assertRaises(ValidationError):
            self.remision.clean()

    def test_datos_validos(self):
        try:
            self.remision.clean()
        except ValidationError:
            self.fail("Datos válidos no deberían lanzar una excepción de validación")