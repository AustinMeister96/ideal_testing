# Generated by Django 4.2.1 on 2023-06-08 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "DataEntry",
            "0010_lab_processing2_remove_lab_processing_da_hs_blk_date_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="Exposure3",
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
                ("home_1_start_yr", models.TextField(max_length=20)),
                ("home_1_end_yr", models.TextField(max_length=20)),
                ("home_1_country", models.TextField(max_length=20)),
                ("home_1_city", models.TextField(max_length=20)),
                ("home_1_province", models.TextField(max_length=20)),
                ("home_1_postal_code", models.TextField(max_length=20)),
                ("home_1_street_address", models.TextField(max_length=20)),
                ("home_1_map_coordinates", models.TextField(max_length=20)),
                ("home_1_avg_monthly_stay", models.TextField(max_length=20)),
                ("home_1_housing_type", models.TextField(max_length=20)),
                ("home_1_housing_type_other", models.TextField(max_length=20)),
                ("home_1_trucks", models.TextField(max_length=20)),
                ("home_1_water_src", models.TextField(max_length=20)),
                ("home_1_water_src_other", models.TextField(max_length=20)),
                ("home_1_heat_src", models.TextField(max_length=20)),
                ("home_1_heat_src_other", models.TextField(max_length=20)),
                ("home_2_start_yr", models.TextField(max_length=20)),
                ("home_2_end_yr", models.TextField(max_length=20)),
                ("home_2_country", models.TextField(max_length=20)),
                ("home_2_city", models.TextField(max_length=20)),
                ("home_2_province", models.TextField(max_length=20)),
                ("home_2_postal_code", models.TextField(max_length=20)),
                ("home_2_street_address", models.TextField(max_length=20)),
                ("home_2_map_coordinates", models.TextField(max_length=20)),
                ("home_2_avg_monthly_stay", models.TextField(max_length=20)),
                ("home_2_housing_type", models.TextField(max_length=20)),
                ("home_2_housing_type_other", models.TextField(max_length=20)),
                ("home_2_trucks", models.TextField(max_length=20)),
                ("home_2_water_src", models.TextField(max_length=20)),
                ("home_2_water_src_other", models.TextField(max_length=20)),
                ("home_2_heat_src", models.TextField(max_length=20)),
                ("home_2_heat_src_other", models.TextField(max_length=20)),
                ("home_3_start_yr", models.TextField(max_length=20)),
                ("home_3_end_yr", models.TextField(max_length=20)),
                ("home_3_country", models.TextField(max_length=20)),
                ("home_3_city", models.TextField(max_length=20)),
                ("home_3_province", models.TextField(max_length=20)),
                ("home_3_postal_code", models.TextField(max_length=20)),
                ("home_3_street_address", models.TextField(max_length=20)),
                ("home_3_map_coordinates", models.TextField(max_length=20)),
                ("home_3_avg_monthly_stay", models.TextField(max_length=20)),
                ("home_3_housing_type", models.TextField(max_length=20)),
                ("home_3_housing_type_other", models.TextField(max_length=20)),
                ("home_3_trucks", models.TextField(max_length=20)),
                ("home_3_water_src", models.TextField(max_length=20)),
                ("home_3_water_src_other", models.TextField(max_length=20)),
                ("home_3_heat_src", models.TextField(max_length=20)),
                ("home_3_heat_src_other", models.TextField(max_length=20)),
                ("home_4_start_yr", models.TextField(max_length=20)),
                ("home_4_end_yr", models.TextField(max_length=20)),
                ("home_4_country", models.TextField(max_length=20)),
                ("home_4_city", models.TextField(max_length=20)),
                ("home_4_province", models.TextField(max_length=20)),
                ("home_4_postal_code", models.TextField(max_length=20)),
                ("home_4_street_address", models.TextField(max_length=20)),
                ("home_4_map_coordinates", models.TextField(max_length=20)),
                ("home_4_avg_monthly_stay", models.TextField(max_length=20)),
                ("home_4_housing_type", models.TextField(max_length=20)),
                ("home_4_housing_type_other", models.TextField(max_length=20)),
                ("home_4_trucks", models.TextField(max_length=20)),
                ("home_4_water_src", models.TextField(max_length=20)),
                ("home_4_water_src_other", models.TextField(max_length=20)),
                ("home_4_heat_src", models.TextField(max_length=20)),
                ("home_4_heat_src_other", models.TextField(max_length=20)),
                ("home_5_start_yr", models.TextField(max_length=20)),
                ("home_5_end_yr", models.TextField(max_length=20)),
                ("home_5_country", models.TextField(max_length=20)),
                ("home_5_city", models.TextField(max_length=20)),
                ("home_5_province", models.TextField(max_length=20)),
                ("home_5_postal_code", models.TextField(max_length=20)),
                ("home_5_street_address", models.TextField(max_length=20)),
                ("home_5_map_coordinates", models.TextField(max_length=20)),
                ("home_5_avg_monthly_stay", models.TextField(max_length=20)),
                ("home_5_housing_type", models.TextField(max_length=20)),
                ("home_5_housing_type_other", models.TextField(max_length=20)),
                ("home_5_trucks", models.TextField(max_length=20)),
                ("home_5_water_src", models.TextField(max_length=20)),
                ("home_5_water_src_other", models.TextField(max_length=20)),
                ("home_5_heat_src", models.TextField(max_length=20)),
                ("home_5_heat_src_other", models.TextField(max_length=20)),
                ("home_6_start_yr", models.TextField(max_length=20)),
                ("home_6_end_yr", models.TextField(max_length=20)),
                ("home_6_country", models.TextField(max_length=20)),
                ("home_6_city", models.TextField(max_length=20)),
                ("home_6_province", models.TextField(max_length=20)),
                ("home_6_postal_code", models.TextField(max_length=20)),
                ("home_6_street_address", models.TextField(max_length=20)),
                ("home_6_map_coordinates", models.TextField(max_length=20)),
                ("home_6_avg_monthly_stay", models.TextField(max_length=20)),
                ("home_6_housing_type", models.TextField(max_length=20)),
                ("home_6_housing_type_other", models.TextField(max_length=20)),
                ("home_6_trucks", models.TextField(max_length=20)),
                ("home_6_water_src", models.TextField(max_length=20)),
                ("home_6_water_src_other", models.TextField(max_length=20)),
                ("home_6_heat_src", models.TextField(max_length=20)),
                ("home_6_heat_src_other", models.TextField(max_length=20)),
            ],
        ),
        migrations.RemoveField(model_name="exposure2", name="home_1_avg_monthly_stay",),
        migrations.RemoveField(model_name="exposure2", name="home_1_city",),
        migrations.RemoveField(model_name="exposure2", name="home_1_country",),
        migrations.RemoveField(model_name="exposure2", name="home_1_end_yr",),
        migrations.RemoveField(model_name="exposure2", name="home_1_heat_src",),
        migrations.RemoveField(model_name="exposure2", name="home_1_heat_src_other",),
        migrations.RemoveField(model_name="exposure2", name="home_1_housing_type",),
        migrations.RemoveField(
            model_name="exposure2", name="home_1_housing_type_other",
        ),
        migrations.RemoveField(model_name="exposure2", name="home_1_map_coordinates",),
        migrations.RemoveField(model_name="exposure2", name="home_1_postal_code",),
        migrations.RemoveField(model_name="exposure2", name="home_1_province",),
        migrations.RemoveField(model_name="exposure2", name="home_1_start_yr",),
        migrations.RemoveField(model_name="exposure2", name="home_1_street_address",),
        migrations.RemoveField(model_name="exposure2", name="home_1_trucks",),
        migrations.RemoveField(model_name="exposure2", name="home_1_water_src",),
        migrations.RemoveField(model_name="exposure2", name="home_1_water_src_other",),
        migrations.RemoveField(model_name="exposure2", name="home_2_avg_monthly_stay",),
        migrations.RemoveField(model_name="exposure2", name="home_2_city",),
        migrations.RemoveField(model_name="exposure2", name="home_2_country",),
        migrations.RemoveField(model_name="exposure2", name="home_2_end_yr",),
        migrations.RemoveField(model_name="exposure2", name="home_2_heat_src",),
        migrations.RemoveField(model_name="exposure2", name="home_2_heat_src_other",),
        migrations.RemoveField(model_name="exposure2", name="home_2_housing_type",),
        migrations.RemoveField(
            model_name="exposure2", name="home_2_housing_type_other",
        ),
        migrations.RemoveField(model_name="exposure2", name="home_2_map_coordinates",),
        migrations.RemoveField(model_name="exposure2", name="home_2_postal_code",),
        migrations.RemoveField(model_name="exposure2", name="home_2_province",),
        migrations.RemoveField(model_name="exposure2", name="home_2_start_yr",),
        migrations.RemoveField(model_name="exposure2", name="home_2_street_address",),
        migrations.RemoveField(model_name="exposure2", name="home_2_trucks",),
        migrations.RemoveField(model_name="exposure2", name="home_2_water_src",),
        migrations.RemoveField(model_name="exposure2", name="home_2_water_src_other",),
        migrations.RemoveField(model_name="exposure2", name="home_3_avg_monthly_stay",),
        migrations.RemoveField(model_name="exposure2", name="home_3_city",),
        migrations.RemoveField(model_name="exposure2", name="home_3_country",),
        migrations.RemoveField(model_name="exposure2", name="home_3_end_yr",),
        migrations.RemoveField(model_name="exposure2", name="home_3_heat_src",),
        migrations.RemoveField(model_name="exposure2", name="home_3_heat_src_other",),
        migrations.RemoveField(model_name="exposure2", name="home_3_housing_type",),
        migrations.RemoveField(
            model_name="exposure2", name="home_3_housing_type_other",
        ),
        migrations.RemoveField(model_name="exposure2", name="home_3_map_coordinates",),
        migrations.RemoveField(model_name="exposure2", name="home_3_postal_code",),
        migrations.RemoveField(model_name="exposure2", name="home_3_province",),
        migrations.RemoveField(model_name="exposure2", name="home_3_start_yr",),
        migrations.RemoveField(model_name="exposure2", name="home_3_street_address",),
        migrations.RemoveField(model_name="exposure2", name="home_3_trucks",),
        migrations.RemoveField(model_name="exposure2", name="home_3_water_src",),
        migrations.RemoveField(model_name="exposure2", name="home_3_water_src_other",),
        migrations.RemoveField(model_name="exposure2", name="home_4_avg_monthly_stay",),
        migrations.RemoveField(model_name="exposure2", name="home_4_city",),
        migrations.RemoveField(model_name="exposure2", name="home_4_country",),
        migrations.RemoveField(model_name="exposure2", name="home_4_end_yr",),
        migrations.RemoveField(model_name="exposure2", name="home_4_heat_src",),
        migrations.RemoveField(model_name="exposure2", name="home_4_heat_src_other",),
        migrations.RemoveField(model_name="exposure2", name="home_4_housing_type",),
        migrations.RemoveField(
            model_name="exposure2", name="home_4_housing_type_other",
        ),
        migrations.RemoveField(model_name="exposure2", name="home_4_map_coordinates",),
        migrations.RemoveField(model_name="exposure2", name="home_4_postal_code",),
        migrations.RemoveField(model_name="exposure2", name="home_4_province",),
        migrations.RemoveField(model_name="exposure2", name="home_4_start_yr",),
        migrations.RemoveField(model_name="exposure2", name="home_4_street_address",),
        migrations.RemoveField(model_name="exposure2", name="home_4_trucks",),
        migrations.RemoveField(model_name="exposure2", name="home_4_water_src",),
        migrations.RemoveField(model_name="exposure2", name="home_4_water_src_other",),
        migrations.RemoveField(model_name="exposure2", name="home_5_avg_monthly_stay",),
        migrations.RemoveField(model_name="exposure2", name="home_5_city",),
        migrations.RemoveField(model_name="exposure2", name="home_5_country",),
        migrations.RemoveField(model_name="exposure2", name="home_5_end_yr",),
        migrations.RemoveField(model_name="exposure2", name="home_5_heat_src",),
        migrations.RemoveField(model_name="exposure2", name="home_5_heat_src_other",),
        migrations.RemoveField(model_name="exposure2", name="home_5_housing_type",),
        migrations.RemoveField(
            model_name="exposure2", name="home_5_housing_type_other",
        ),
        migrations.RemoveField(model_name="exposure2", name="home_5_map_coordinates",),
        migrations.RemoveField(model_name="exposure2", name="home_5_postal_code",),
        migrations.RemoveField(model_name="exposure2", name="home_5_province",),
        migrations.RemoveField(model_name="exposure2", name="home_5_start_yr",),
        migrations.RemoveField(model_name="exposure2", name="home_5_street_address",),
        migrations.RemoveField(model_name="exposure2", name="home_5_trucks",),
        migrations.RemoveField(model_name="exposure2", name="home_5_water_src",),
        migrations.RemoveField(model_name="exposure2", name="home_5_water_src_other",),
        migrations.RemoveField(model_name="exposure2", name="home_6_avg_monthly_stay",),
        migrations.RemoveField(model_name="exposure2", name="home_6_city",),
        migrations.RemoveField(model_name="exposure2", name="home_6_country",),
        migrations.RemoveField(model_name="exposure2", name="home_6_end_yr",),
        migrations.RemoveField(model_name="exposure2", name="home_6_heat_src",),
        migrations.RemoveField(model_name="exposure2", name="home_6_heat_src_other",),
        migrations.RemoveField(model_name="exposure2", name="home_6_housing_type",),
        migrations.RemoveField(
            model_name="exposure2", name="home_6_housing_type_other",
        ),
        migrations.RemoveField(model_name="exposure2", name="home_6_map_coordinates",),
        migrations.RemoveField(model_name="exposure2", name="home_6_postal_code",),
        migrations.RemoveField(model_name="exposure2", name="home_6_province",),
        migrations.RemoveField(model_name="exposure2", name="home_6_start_yr",),
        migrations.RemoveField(model_name="exposure2", name="home_6_street_address",),
        migrations.RemoveField(model_name="exposure2", name="home_6_trucks",),
        migrations.RemoveField(model_name="exposure2", name="home_6_water_src",),
        migrations.RemoveField(model_name="exposure2", name="home_6_water_src_other",),
    ]
