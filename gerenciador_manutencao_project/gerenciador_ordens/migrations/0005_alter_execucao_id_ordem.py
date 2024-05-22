# Generated by Django 5.0.1 on 2024-05-08 22:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("abertura_ordem", "0010_alter_maquina_setor_alter_ordens_maquina_and_more"),
        ("gerenciador_ordens", "0004_remove_execucao_operadores_execucao_operadores"),
    ]

    operations = [
        migrations.AlterField(
            model_name="execucao",
            name="id_ordem",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="execucao_id_ordem",
                to="abertura_ordem.ordens",
            ),
        ),
    ]
