# Generated by Django 4.1.4 on 2023-02-18 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0006_alter_patientappointmentanswer_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='patients',
            options={'ordering': ['-id'], 'verbose_name': 'Appointment'},
        ),
    ]