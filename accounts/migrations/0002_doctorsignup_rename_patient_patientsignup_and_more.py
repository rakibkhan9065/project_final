# Generated by Django 4.1.4 on 2022-12-17 11:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorSignUp',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('hospital', models.CharField(max_length=110)),
                ('education', models.CharField(max_length=255)),
            ],
        ),
        migrations.RenameModel(
            old_name='Patient',
            new_name='PatientSignUp',
        ),
        migrations.DeleteModel(
            name='Doctor',
        ),
    ]
