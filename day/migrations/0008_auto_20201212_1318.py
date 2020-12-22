# Generated by Django 3.1.4 on 2020-12-12 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '__first__'),
        ('day', '0007_auto_20201212_1310'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='hour',
            unique_together={('patientId', 'hour', 'dayId'), ('patientId', 'dayId'), ('hour', 'dayId')},
        ),
    ]
