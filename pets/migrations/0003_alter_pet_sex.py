# Generated by Django 4.1.3 on 2022-12-05 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pets", "0002_alter_pet_group"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pet",
            name="sex",
            field=models.CharField(
                choices=[
                    ("Male", "Male"),
                    ("Female", "Female"),
                    ("Not Informed", "Default"),
                ],
                default="Not Informed",
                max_length=20,
            ),
        ),
    ]