# Generated by Django 5.0.1 on 2024-05-08 21:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "abertura_ordem",
            "0007_alter_maquina_setor_maquina_solda_alter_ordens_foto_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="AreaManutencao",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="TipoManutencao",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=200)),
            ],
        ),
    ]
