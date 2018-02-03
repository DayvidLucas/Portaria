# Generated by Django 2.0.2 on 2018-02-03 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Onibus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('empresa', models.CharField(max_length=50, verbose_name='Empresa')),
                ('trajeto', models.CharField(choices=[('MP', 'Mendes x Pirai'), ('PB', 'Pirai x B.Pirai'), ('BP', 'B.Pirai x Pirai'), ('MP', 'Mendes x Pirai'), ('PM', 'Pirai x Mendes')], max_length=2, verbose_name='Autorizado por')),
                ('passageiro', models.IntegerField(max_length=4, verbose_name='Passageiros (qnt)')),
                ('placa', models.CharField(max_length=7, verbose_name='Placa')),
                ('entrada', models.DateTimeField(verbose_name='Chegada')),
                ('saida', models.DateTimeField(blank=True, null=True, verbose_name='Hora de saida')),
                ('observacao', models.TextField(blank=True, null=True, verbose_name='Observação')),
            ],
            options={
                'verbose_name': 'Onibus',
                'verbose_name_plural': 'Onibus',
            },
        ),
    ]
