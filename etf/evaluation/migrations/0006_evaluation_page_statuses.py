# Generated by Django 3.2.18 on 2023-02-21 15:50

from django.db import migrations, models

import etf.evaluation.pages


class Migration(migrations.Migration):
    dependencies = [
        ("evaluation", "0005_alter_evaluation_users"),
    ]

    operations = [
        migrations.AddField(
            model_name="evaluation",
            name="page_statuses",
            field=models.JSONField(default=etf.evaluation.pages.get_default_page_statuses),
        ),
    ]
