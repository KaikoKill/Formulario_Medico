# Generated by Django 5.1.4 on 2024-12-19 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Datos', '0005_alter_remisioncaso_firma_medico_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remisioncaso',
            name='firma_medico',
            field=models.FileField(upload_to='firma_medico/'),
        ),
    ]
