# Generated by Django 3.2.16 on 2022-11-17 22:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("evaluation", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="intervention",
            name="provider_description",
            field=models.TextField(
                blank=True,
                null=True,
                verbose_name="For each category of intervention provider (e.g. housing officer) description of their expertise, background and any specific training they will receive",
            ),
        ),
        migrations.AlterField(
            model_name="intervention",
            name="frequency_of_delivery",
            field=models.TextField(
                blank=True,
                null=True,
                verbose_name="Description of the number of times the intervention will be delivered and over what time period including the number of sessions, their schedule, and their duration or intensity. Number of sessions might be determined by some stopping criteria rather than a fixed number, in which case provide details.",
            ),
        ),
        migrations.AlterField(
            model_name="intervention",
            name="location",
            field=models.TextField(
                blank=True,
                null=True,
                verbose_name="Description of the type(s) of location(s) where the intervention will occur, including necessary infrastructure or relevant features",
            ),
        ),
        migrations.AlterField(
            model_name="intervention",
            name="modes_of_delivery",
            field=models.TextField(
                blank=True,
                null=True,
                verbose_name="Description of modes of delivery (e.g. face-to-face, telephone) of the intervention and whether it will be provided individually or in a group",
            ),
        ),
    ]
