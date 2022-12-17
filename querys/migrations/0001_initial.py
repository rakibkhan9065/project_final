# Generated by Django 4.1.4 on 2022-12-17 13:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=20)),
                ('post', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(blank=True, default='', max_length=100)),
                ('query', models.TextField(blank=True, default='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='AnswerPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('answer_text', models.TextField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='querys.post')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(blank=True, default='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='answer', to=settings.AUTH_USER_MODEL)),
                ('query', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='answer', to='querys.query')),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]
