# Generated by Django 4.2.7 on 2023-11-21 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SourceCategory",
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
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Source",
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
                ("telegram_name", models.CharField(max_length=255)),
                (
                    "language",
                    models.CharField(
                        choices=[("tamil", "Tamil"), ("english", "English")],
                        max_length=10,
                    ),
                ),
                (
                    "level",
                    models.CharField(
                        choices=[
                            ("Basic", "Basic"),
                            ("Intermediate", "Intermediate"),
                            ("Advanced", "Advanced"),
                            ("Project Based", "Project Based"),
                            ("Topic Based", "Topic Based"),
                        ],
                        max_length=100,
                    ),
                ),
                ("channel_name", models.CharField(max_length=255)),
                ("link", models.URLField()),
                ("total_hits", models.PositiveIntegerField(default=0)),
                ("feedback", models.TextField(blank=True, null=True)),
                ("ratings", models.PositiveIntegerField(default=0)),
                ("total_ratings", models.PositiveIntegerField(default=0)),
                ("total_rating_count", models.PositiveIntegerField(default=0)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ProjApp.sourcecategory",
                    ),
                ),
            ],
        ),
    ]