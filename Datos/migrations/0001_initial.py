# Generated by Django 5.1.3 on 2025-02-06 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RemisionCaso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unidad', models.CharField(max_length=100)),
                ('no_historia_clinica_individual', models.CharField(max_length=50)),
                ('no_historia_clinica_hospital_base', models.CharField(max_length=50)),
                ('consultorio_medico_familia', models.CharField(max_length=50)),
                ('referido_a', models.CharField(max_length=100)),
                ('fecha_turno_programado', models.DateField()),
                ('hora_turno_programado', models.TimeField()),
                ('sexo', models.CharField(choices=[('Femenino', 'Femenino'), ('Masculino', 'Masculino')], max_length=10)),
                ('edad', models.PositiveIntegerField()),
                ('color_piel', models.CharField(choices=[('Blanca', 'Blanca'), ('Negra', 'Negra'), ('Mestiza', 'Mestiza')], max_length=10)),
                ('nacimiento', models.CharField(default='null', max_length=100)),
                ('fecha_nacimiento', models.DateField()),
                ('nombre', models.CharField(max_length=100)),
                ('primer_apellido', models.CharField(max_length=100)),
                ('segundo_apellido', models.CharField(max_length=100)),
                ('residencia_habitual', models.CharField(max_length=255)),
                ('apartamento', models.CharField(max_length=255)),
                ('no_o_km', models.CharField(max_length=50)),
                ('edificio', models.CharField(max_length=50)),
                ('direccion_entre_calles', models.CharField(max_length=100)),
                ('localidad', models.CharField(max_length=100)),
                ('provincia', models.CharField(max_length=100)),
                ('municipio', models.CharField(max_length=100)),
                ('telefono', models.CharField(blank=True, max_length=20, null=True)),
                ('nombre_padre', models.CharField(max_length=100)),
                ('nombre_madre', models.CharField(max_length=100)),
                ('estado_vital_padre', models.CharField(choices=[('Vivo', 'Vivo'), ('Muerto', 'Muerto')], max_length=10)),
                ('estado_vital_madre', models.CharField(choices=[('Vivo', 'Vivo'), ('Muerto', 'Muerto')], max_length=10)),
                ('referido_a_especialista_de', models.CharField(max_length=100)),
                ('antecedentes_interes', models.TextField()),
                ('resumen_sindromico', models.TextField()),
                ('resumen_examen_fisico', models.TextField()),
                ('tratamiento', models.TextField()),
                ('evolucion', models.TextField()),
                ('impresion_diagnostica', models.TextField()),
                ('otros_diagnosticos', models.TextField(blank=True, null=True)),
                ('nombre_medico', models.CharField(max_length=100)),
                ('firma_medico', models.ImageField(blank=True, null=True, upload_to='firma_medico/')),
                ('fecha', models.DateField()),
            ],
        ),
    ]
