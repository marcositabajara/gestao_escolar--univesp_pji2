# Generated by Django 4.0.4 on 2022-06-29 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escolar', '0003_alter_cadastro_matricula_alter_disciplina_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diario',
            name='ano_semestre',
            field=models.CharField(max_length=8, null=True),
        ),
    ]