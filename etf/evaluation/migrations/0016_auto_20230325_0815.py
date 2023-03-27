# Generated by Django 3.2.18 on 2023-03-25 08:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("evaluation", "0015_evaluation_search_text"),
    ]

    operations = [
        migrations.AddField(
            model_name="document",
            name="document_type_other",
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="evaluation",
            name="evaluation_type_other",
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="evaluation",
            name="impact_eval_basis_other",
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="evaluation",
            name="impact_eval_design_name_other",
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="evaluation",
            name="impact_eval_effect_measure_interval_other",
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="evaluation",
            name="impact_eval_framework_other",
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="evaluation",
            name="impact_eval_interpretation_type_other",
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="othermeasure",
            name="measure_type_other",
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="outcomemeasure",
            name="measure_type_other",
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
