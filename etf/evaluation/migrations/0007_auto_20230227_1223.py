# Generated by Django 3.2.18 on 2023-02-27 12:23

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("evaluation", "0006_auto_20230227_1201"),
    ]

    operations = [
        migrations.RenameField(
            model_name="eventdate",
            old_name="name",
            new_name="event_date_name",
        ),
        migrations.RenameField(
            model_name="eventdate",
            old_name="type",
            new_name="event_date_type",
        ),
    ]