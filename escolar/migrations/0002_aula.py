# Generated by Django 4.0.4 on 2022-06-28 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('escolar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordem_aula', models.IntegerField(null=True)),
                ('data_aula', models.DateField(null=True)),
                ('descricao', models.CharField(max_length=300, null=True)),
                ('diario_fk', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='escolar.diario')),
            ],
        ),
    ]
