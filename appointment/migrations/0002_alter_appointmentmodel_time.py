# Generated by Django 5.1 on 2024-09-02 06:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
        ('doctor', '0004_alter_reviewmodel_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointmentmodel',
            name='time',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.doctoravailabletime'),
        ),
    ]
