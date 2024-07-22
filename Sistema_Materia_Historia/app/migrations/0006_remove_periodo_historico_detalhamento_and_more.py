# Generated by Django 5.0.7 on 2024-07-22 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_periodo_historico_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='periodo_historico',
            name='detalhamento',
        ),
        migrations.AddField(
            model_name='periodo_historico',
            name='contexto',
            field=models.TextField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='periodo_historico',
            name='impactos',
            field=models.TextField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='periodo_historico',
            name='legado',
            field=models.TextField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='periodo_historico',
            name='principais',
            field=models.TextField(max_length=10000, null=True),
        ),
    ]
