# Generated by Django 3.2.18 on 2023-03-26 00:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("evaluation", "0020_alter_processstandard_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="intervention",
            name="name",
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
    ]