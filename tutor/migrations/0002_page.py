# Generated by Django 4.1.6 on 2023-04-11 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tutor", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Page",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("page_source", models.TextField()),
                ("page_number", models.CharField(max_length=10)),
                ("page_content", models.TextField()),
            ],
        ),
    ]