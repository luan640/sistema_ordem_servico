# Generated by Django 5.0.1 on 2024-05-08 21:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("gerenciador_ordens", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="execucao",
            name="n_execucao",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
