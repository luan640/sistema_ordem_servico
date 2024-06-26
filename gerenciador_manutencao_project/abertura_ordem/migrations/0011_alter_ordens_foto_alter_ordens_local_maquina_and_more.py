# Generated by Django 5.0.1 on 2024-05-11 09:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("abertura_ordem", "0010_alter_maquina_setor_alter_ordens_maquina_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ordens",
            name="foto",
            field=models.ImageField(null=True, upload_to="photo/"),
        ),
        migrations.AlterField(
            model_name="ordens",
            name="local_maquina",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="ordens",
            name="setor_maquina_solda",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="ordens_maquina_solda",
                to="abertura_ordem.maquinasolda",
            ),
        ),
        migrations.AlterField(
            model_name="ordens",
            name="video",
            field=models.ImageField(null=True, upload_to="video/"),
        ),
    ]
