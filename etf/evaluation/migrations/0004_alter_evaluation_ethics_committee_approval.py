# Generated by Django 3.2.18 on 2023-02-25 09:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("evaluation", "0003_delete_evaluationtype"),
    ]

    operations = [
        migrations.AlterField(
            model_name="evaluation",
            name="ethics_committee_approval",
            field=models.CharField(blank=True, choices=[("YES", "Yes"), ("NO", "No")], max_length=3, null=True),
        ),
    ]
