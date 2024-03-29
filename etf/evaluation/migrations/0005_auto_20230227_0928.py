# Generated by Django 3.2.18 on 2023-02-27 09:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("evaluation", "0004_alter_evaluation_ethics_committee_approval"),
    ]

    operations = [
        migrations.RenameField(
            model_name="evaluation",
            old_name="impact_eval_effect_measure",
            new_name="economic_eval_design_details",
        ),
        migrations.AddField(
            model_name="evaluation",
            name="impact_eval_desc_planned_analysis",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="evaluation",
            name="impact_eval_lower_uncertainty",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="evaluation",
            name="impact_eval_missing_data_handling",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="evaluation",
            name="impact_eval_point_estimate_diff",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="evaluation",
            name="impact_eval_primary_effect_size_desc",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="evaluation",
            name="impact_eval_primary_effect_size_measure",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="evaluation",
            name="impact_eval_sensitivity_analysis",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="evaluation",
            name="impact_eval_subgroup_analysis",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="evaluation",
            name="impact_eval_upper_uncertainty",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="evaluation",
            name="monetisation_approaches",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="evaluation",
            name="perspective_benefits",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="evaluation",
            name="perspective_costs",
            field=models.TextField(blank=True, null=True),
        ),
    ]
