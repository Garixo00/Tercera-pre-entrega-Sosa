# Generated by Django 5.0.6 on 2024-07-30 04:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appproyecto3pe', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evaluacion',
            name='visto_asesor',
        ),
    ]