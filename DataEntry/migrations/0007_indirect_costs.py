# Generated by Django 4.2.3 on 2024-01-29 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DataEntry', '0006_remove_mandatory_questionaire_biological_relatives_cancer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Indirect_costs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_date', models.DateField()),
                ('procedure', models.TextField(choices=[('Spiral CT', 'Spiral CT'), ('Spirometry', 'Spirometry'), ('Blood Collection', 'Blood Collection'), ('Other', 'Other')], max_length=20)),
                ('procedure_other', models.TextField(choices=[('Spiral CT', 'Spiral CT'), ('Spirometry', 'Spirometry'), ('Blood Collection', 'Blood Collection'), ('Other', 'Other')], max_length=100)),
                ('participant_num', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DataEntry.participant')),
            ],
        ),
    ]
