# Generated by Django 3.2.18 on 2023-03-21 13:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("evaluation", "0014_auto_20230312_1710"),
    ]

    operations = [
        migrations.AddField(
            model_name="evaluation",
            name="search_text",
            field=models.TextField(blank=True, max_length=65536, null=True),
        ),
    ]