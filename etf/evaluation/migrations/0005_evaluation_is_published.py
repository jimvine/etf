# Generated by Django 3.2.16 on 2022-12-20 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("evaluation", "0004_auto_20221219_0808"),
    ]

    operations = [
        migrations.AddField(
            model_name="evaluation",
            name="is_published",
            field=models.BooleanField(blank=True, null=True),
        ),
    ]