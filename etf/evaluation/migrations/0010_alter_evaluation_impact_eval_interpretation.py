# Generated by Django 3.2.18 on 2023-02-27 15:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("evaluation", "0009_auto_20230227_1339"),
    ]

    operations = [
        migrations.AlterField(
            model_name="evaluation",
            name="impact_eval_interpretation",
            field=models.CharField(
                blank=True,
                choices=[
                    ("SUPERIORITY_SUPERIOR", "Superiority framework: Superior"),
                    ("SUPERIORITY_INFERIOR", "Superiority framework: Inferior"),
                    ("SUPERIORITY_INCONCLUSIVE", "Superiority framework: Inconclusive"),
                    ("NON_INFERIORITY_SUPERIOR", "Non-inferiority framework: Superior"),
                    ("NON_INFERIORITY_NON_INFERIOR", "Non-inferiority framework: Non-inferior"),
                    ("NON_INFERIORITY_INFERIOR", "Non-inferiority framework: Inferior"),
                    ("NON_INFERIORITY_INCONCLUSIVE", "Non-inferiority framework: Inconclusive"),
                    ("EQUIVALENCE_EQUIVALENT", "Equivalence framework: Equivalent"),
                    ("EQUIVALENCE_NON_EQUIVALENT", "Equivalence framework: Non-equivalent"),
                    ("EQUIVALENCE_NON_EQUIVALENT_SUPERIOR", "Equivalence framework: Non-equivalent (superior)"),
                    ("EQUIVALENCE_NON_EQUIVALENT_INFERIOR", "Equivalence framework: Non-equivalent (inferior)"),
                    ("EQUIVALENCE_NON_EQUIVALENT_INCONCLUSIVE", "Equivalence framework: Inconclusive"),
                    ("OTHER", "Other"),
                ],
                max_length=256,
                null=True,
            ),
        ),
    ]