# Generated by Django 3.1.4 on 2020-12-22 15:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_auto_20201206_1615'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('patient', '0003_merge_20201222_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorpatient',
            name='doctorId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patients', to='doctor.doctor'),
        ),
        migrations.AlterField(
            model_name='doctorpatient',
            name='patientId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctors', to='patient.patient'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='userId',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='patient', to=settings.AUTH_USER_MODEL),
        ),
    ]
