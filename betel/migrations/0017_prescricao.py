# Generated by Django 4.1.1 on 2022-10-02 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('betel', '0016_medicacao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prescricao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_da_prescricao', models.DateField(blank=True, null=True)),
                ('medico_responsavel', models.CharField(blank=True, help_text='Insira o nome do médico', max_length=50, null=True)),
                ('enfermeiro_responsavel', models.CharField(blank=True, help_text='Insira o nome do enfermeiro', max_length=50, null=True)),
                ('dose', models.FloatField(blank=True, null=True)),
                ('horario', models.TimeField(blank=True, null=True)),
                ('repeticao', models.CharField(blank=True, choices=[('D', 'Diária'), ('S', 'Semanal'), ('M', 'Mensal'), ('A', 'Anual'), ('N', 'Não se repete')], max_length=1, null=True)),
                ('segunda', models.BooleanField(null=True)),
                ('terca', models.BooleanField(null=True)),
                ('quarta', models.BooleanField(null=True)),
                ('quinta', models.BooleanField(null=True)),
                ('sexta', models.BooleanField(null=True)),
                ('sabado', models.BooleanField(null=True)),
                ('domingo', models.BooleanField(null=True)),
                ('data_de_inicio', models.DateField(blank=True, null=True)),
                ('duracao', models.CharField(blank=True, choices=[('CON', 'Contínua'), ('DUR', 'Durante...'), ('ATE', 'Até a data')], max_length=3, null=True)),
                ('dias_de_duracao', models.PositiveIntegerField(blank=True, null=True)),
                ('data_final', models.DateField(blank=True, null=True)),
                ('hospede', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='betel.hospede')),
                ('medicacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='betel.medicacao')),
            ],
        ),
    ]
