# Generated by Django 4.1.1 on 2022-10-02 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('betel', '0015_alter_evolucao_evolucao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, help_text='Insira o nome do remédio', max_length=50, null=True)),
                ('quantidade', models.PositiveIntegerField(blank=True, null=True)),
                ('unidade', models.CharField(blank=True, choices=[('mg', 'miligrama'), ('UI', 'Unidades Internacionais')], max_length=10, null=True)),
                ('fabricante', models.CharField(blank=True, max_length=25, null=True)),
                ('generico', models.BooleanField(null=True)),
            ],
        ),
    ]
