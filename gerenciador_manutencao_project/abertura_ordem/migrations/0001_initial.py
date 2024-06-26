# Generated by Django 4.2.13 on 2024-05-08 01:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Maquina',
            fields=[
                ('nome', models.CharField(max_length=100)),
                ('codigo', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('tombamento', models.CharField(max_length=200)),
                ('apelido', models.CharField(max_length=200)),
                ('descricao', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MaquinaSolda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Operador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('matricula', models.CharField(max_length=200)),
                ('salario', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Setor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Solicitantes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('matricula', models.CharField(max_length=200)),
                ('setor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solicitante_setor', to='abertura_ordem.setor')),
            ],
        ),
        migrations.CreateModel(
            name='Ordens',
            fields=[
                ('id_ordem', models.AutoField(primary_key=True, serialize=False)),
                ('local_maquina', models.CharField(max_length=200)),
                ('descricao', models.CharField(max_length=200)),
                ('impacto_producao', models.CharField(choices=[('alto', 'Alto'), ('baixo', 'Baixo'), ('medio', 'Médio')], max_length=20)),
                ('maquina_parada', models.BooleanField(default=False)),
                ('data_hora_abertura', models.DateTimeField(auto_now_add=True)),
                ('foto', models.URLField(blank=True, null=True)),
                ('video', models.URLField(blank=True, null=True)),
                ('maquina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordens_maquina', to='abertura_ordem.maquina')),
                ('setor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordens_setor', to='abertura_ordem.setor')),
                ('setor_maquina_solda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordens_maquina_solda', to='abertura_ordem.maquinasolda')),
                ('solicitante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordens_solicitantes', to='abertura_ordem.solicitantes')),
            ],
        ),
        migrations.AddField(
            model_name='maquinasolda',
            name='setor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='maquina_solda_setor', to='abertura_ordem.setor'),
        ),
        migrations.AddField(
            model_name='maquina',
            name='setor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='maquina_setor', to='abertura_ordem.setor'),
        ),
        migrations.AddField(
            model_name='maquina',
            name='setor_maquina_solda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='maquina_setor_solda', to='abertura_ordem.maquinasolda'),
        ),
    ]
