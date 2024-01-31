# Generated by Django 4.2.3 on 2024-01-29 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DataEntry', '0008_alter_indirect_costs_procedure_other'),
    ]

    operations = [
        migrations.AddField(
            model_name='indirect_costs',
            name='affected_pay',
            field=models.TextField(choices=[('It affected by pay', 'It affected by pay'), ('It was time granted by my employer', 'It was time granted by my employer')], default=None, max_length=50, null=True, verbose_name='Other Procedure'),
        ),
        migrations.AddField(
            model_name='indirect_costs',
            name='appointment_time_hours',
            field=models.FloatField(blank=True, null=True, verbose_name='Appointment Time Hours'),
        ),
        migrations.AddField(
            model_name='indirect_costs',
            name='appointment_time_minutes',
            field=models.FloatField(blank=True, null=True, verbose_name='Appointment Time Minutes'),
        ),
        migrations.AddField(
            model_name='indirect_costs',
            name='babysitter_cost',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='indirect_costs',
            name='income',
            field=models.TextField(blank=True, choices=[('< $10,000', '< $10,000'), ('$10,000 to $19,999', '$10,000 to $19,999'), ('$20,000 to $29,999', '$20,000 to $29,999'), ('$30,000 to $39,999', '$30,000 to $39,999'), ('$40,000 to $49,999', '$40,000 to $49,999'), ('$50,000 to $59,999', '$50,000 to $59,999'), ('$60,000 to $69,999', '$60,000 to $69,999'), ('$70,000 to $79,999', '$70,000 to $79,999'), ('$80,000 to $89,999', '$80,000 to $89,999'), ('$90,000 to $99,999', '$90,000 to $99,999'), ('$100,000 to $124,999', '$100,000 to $124,999'), ('$125,000 to $149,999', '$125,000 to $149,999'), ('≥ $150,000', '≥ $150,000')], max_length=40, verbose_name='What is your annual income (gross income, before taxes)?'),
        ),
        migrations.AddField(
            model_name='indirect_costs',
            name='income_household',
            field=models.TextField(blank=True, choices=[('< $10,000', '< $10,000'), ('$10,000 to $19,999', '$10,000 to $19,999'), ('$20,000 to $29,999', '$20,000 to $29,999'), ('$30,000 to $39,999', '$30,000 to $39,999'), ('$40,000 to $49,999', '$40,000 to $49,999'), ('$50,000 to $59,999', '$50,000 to $59,999'), ('$60,000 to $69,999', '$60,000 to $69,999'), ('$70,000 to $79,999', '$70,000 to $79,999'), ('$80,000 to $89,999', '$80,000 to $89,999'), ('$90,000 to $99,999', '$90,000 to $99,999'), ('$100,000 to $124,999', '$100,000 to $124,999'), ('$125,000 to $149,999', '$125,000 to $149,999'), ('≥ $150,000', '≥ $150,000')], max_length=40, verbose_name='What is the annual income of your household (gross income, before taxes)?'),
        ),
        migrations.AddField(
            model_name='indirect_costs',
            name='missed_work',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, max_length=50, verbose_name='Did you miss work to attend this medical appointment?'),
        ),
        migrations.AddField(
            model_name='indirect_costs',
            name='missed_work_hours',
            field=models.FloatField(blank=True, null=True, verbose_name='How many hours of work did you miss today to attend your appointment?'),
        ),
        migrations.AddField(
            model_name='indirect_costs',
            name='other_cost',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='indirect_costs',
            name='other_costs_description',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='indirect_costs',
            name='parking_cost',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='indirect_costs',
            name='public_transportation_cost',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='indirect_costs',
            name='transportation',
            field=models.TextField(choices=[('Private: (car)', 'Private: (car)'), ('Public transportation (bus, metro, train, taxi)', 'Public transportation (bus, metro, train, taxi)')], default=None, max_length=50, verbose_name='What means of transportation did you use to come to this appointment?'),
        ),
        migrations.AddField(
            model_name='indirect_costs',
            name='trip_distance',
            field=models.FloatField(blank=True, null=True, verbose_name='Estimate the round trip distance in kilometers'),
        ),
        migrations.AlterField(
            model_name='indirect_costs',
            name='procedure',
            field=models.TextField(choices=[('Spiral CT', 'Spiral CT'), ('Spirometry', 'Spirometry'), ('Blood Collection', 'Blood Collection'), ('Other', 'Other')], default=None, max_length=20, verbose_name='What procedure(s) have you come in for?'),
        ),
        migrations.AlterField(
            model_name='indirect_costs',
            name='procedure_other',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='Other Procedure'),
        ),
    ]