# Generated by Django 4.2.4 on 2023-11-20 05:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("AppOfJeju", "0002_cropmarketdata"),
    ]

    operations = [
        migrations.AddField(
            model_name="cropmarketdata",
            name="origin",
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
