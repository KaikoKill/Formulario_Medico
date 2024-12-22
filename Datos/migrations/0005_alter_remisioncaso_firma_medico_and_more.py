# Generated by Django 5.1.4 on 2024-12-19 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Datos', '0004_remisioncaso_nacimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remisioncaso',
            name='firma_medico',
            field=models.ImageField(upload_to='firma_medico/'),
        ),
        migrations.AlterField(
            model_name='remisioncaso',
            name='sexo',
            field=models.CharField(choices=[('Femenino', 'Femenino'), ('Masculino', 'Masculino')], max_length=10),
        ),
    ]