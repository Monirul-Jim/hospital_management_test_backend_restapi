# Generated by Django 5.1 on 2024-09-01 05:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_remove_doctormodel_available_time_and_more'),
        ('patient', '0002_alter_patientmodel_options_alter_patientmodel_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('rating', models.CharField(choices=[('*', '*'), ('* *', '* *'), ('* * *', '* * *'), ('* * * *', '* * * *'), ('* * * * *', '* * * * *')], max_length=10)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.doctormodel')),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patientmodel')),
            ],
        ),
    ]
