# Generated by Django 5.1.4 on 2024-12-18 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Datos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remisioncaso',
            name='firma_medico',
            field=models.FileField(upload_to=''),
        ),
    ]