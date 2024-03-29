# Generated by Django 4.2.3 on 2024-01-23 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("DataEntry", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mandatory_questionaire",
            name="biological_relatives_cancer",
            field=models.TextField(
                blank=True,
                choices=[("Yes", "Yes"), ("No", "No"), ("Dont know", "Dont know")],
                max_length=25,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="mandatory_questionaire",
            name="current_height_unit",
            field=models.TextField(
                choices=[("cm", "cm"), ("inches", "in")], max_length=20
            ),
        ),
    ]
