# Generated by Django 4.1.3 on 2022-12-06 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("groups", "0004_alter_group_scientific_name"),
        ("pets", "0003_alter_pet_sex"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pet",
            name="group",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="pets",
                to="groups.group",
            ),
        ),
    ]
