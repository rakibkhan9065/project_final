# Generated by Django 4.1.3 on 2022-11-13 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helper', '0002_createquery_created_at_createquery_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createquery',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='createquery',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
