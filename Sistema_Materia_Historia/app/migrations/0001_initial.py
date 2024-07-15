# Generated by Django 5.0.7 on 2024-07-15 11:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('detalhamento', models.TextField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'Diciplina',
            },
        ),
        migrations.CreateModel(
            name='Topico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Topico',
            },
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Turma',
            },
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('topico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.topico')),
            ],
            options={
                'verbose_name_plural': 'Professor',
            },
        ),
        migrations.CreateModel(
            name='Periodo_Historico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalhamento', models.TextField(max_length=500)),
                ('topico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.topico')),
            ],
            options={
                'verbose_name_plural': 'Periodo_Historico',
            },
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('matricula', models.DecimalField(decimal_places=8, max_digits=10)),
                ('datanasc', models.DateField()),
                ('turma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.turma')),
            ],
            options={
                'verbose_name_plural': 'Aluno',
            },
        ),
    ]
