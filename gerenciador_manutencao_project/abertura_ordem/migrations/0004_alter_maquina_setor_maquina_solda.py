# Generated by Django 4.2.13 on 2024-05-08 01:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('abertura_ordem', '0003_alter_maquinasolda_setor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maquina',
            name='setor_maquina_solda',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='maquina_setor_solda', to='abertura_ordem.maquinasolda'),
        ),
    ]
