# Generated by Django 4.2.13 on 2024-05-08 01:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('abertura_ordem', '0004_alter_maquina_setor_maquina_solda'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordens',
            name='local_maquina',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='ordens',
            name='setor_maquina_solda',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ordens_maquina_solda', to='abertura_ordem.maquinasolda'),
        ),
    ]
