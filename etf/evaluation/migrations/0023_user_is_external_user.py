# Generated by Django 3.2.18 on 2023-04-12 12:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("evaluation", "0022_auto_20230410_0825"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="is_external_user",
            field=models.BooleanField(default=False),
        ),
    ]