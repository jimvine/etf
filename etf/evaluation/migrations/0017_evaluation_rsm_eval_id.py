# Generated by Django 3.2.18 on 2023-03-25 17:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("evaluation", "0016_auto_20230325_0815"),
    ]

    operations = [
        migrations.AddField(
            model_name="evaluation",
            name="rsm_eval_id",
            field=models.FloatField(blank=True, null=True),
        ),
    ]
