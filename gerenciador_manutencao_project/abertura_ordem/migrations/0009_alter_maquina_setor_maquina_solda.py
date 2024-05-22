# Generated by Django 5.0.1 on 2024-05-08 19:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("abertura_ordem", "0008_areamanutencao_tipomanutencao"),
    ]

    operations = [
        migrations.AlterField(
            model_name="maquina",
            name="setor_maquina_solda",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="maquina_setor_solda",
                to="abertura_ordem.maquinasolda",
            ),
        ),
    ]