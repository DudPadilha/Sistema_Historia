# Generated by Django 5.0.7 on 2024-07-22 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_curso_turma_remove_aluno_turma_aluno_curso_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='periodo_historico',
            options={'verbose_name_plural': 'Periodos_Historicos'},
        ),
        migrations.RemoveField(
            model_name='periodo_historico',
            name='data',
        ),
        migrations.AddField(
            model_name='periodo_historico',
            name='seculo',
            field=models.CharField(max_length=100, null=True),
        ),
    ]