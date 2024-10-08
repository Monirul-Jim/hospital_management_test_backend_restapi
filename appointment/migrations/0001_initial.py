# Generated by Django 5.1 on 2024-09-01 05:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctor', '0004_alter_reviewmodel_rating'),
        ('patient', '0002_alter_patientmodel_options_alter_patientmodel_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppointmentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_types', models.CharField(choices=[('Offline', 'Offline'), ('Online', 'Online')], max_length=10)),
                ('appointment_status', models.CharField(choices=[('Completed', 'Completed'), ('Pending', 'Pending'), ('Running', 'Running')], default='Pending', max_length=10)),
                ('symptoms', models.TextField()),
                ('cancel', models.BooleanField(default=False)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.doctormodel')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patientmodel')),
                ('time', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='doctor.doctoravailabletime')),
            ],
        ),
    ]
