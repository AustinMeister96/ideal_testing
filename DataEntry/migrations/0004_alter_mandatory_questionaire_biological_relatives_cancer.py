# Generated by Django 4.2.3 on 2024-01-23 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "DataEntry",
            "0003_alter_mandatory_questionaire_biological_relatives_cancer_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="mandatory_questionaire",
            name="biological_relatives_cancer",
            field=models.TextField(
                blank=True,
                choices=[(True, "Yes"), (False, "No"), (None, "Don't Know")],
                max_length=25,
                null=True,
            ),
        ),
    ]