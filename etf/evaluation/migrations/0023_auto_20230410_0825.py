# Generated by Django 3.2.18 on 2023-04-10 08:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("evaluation", "0022_create_third_party_user_group"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="invite_accepted_at",
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="invited_at",
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
