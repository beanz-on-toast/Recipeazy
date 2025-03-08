# Generated by Django 5.1.7 on 2025-03-08 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0002_remove_recipe_prep_time"),
    ]

    operations = [
        migrations.AddField(
            model_name="recipe",
            name="difficulty",
            field=models.CharField(
                choices=[
                    ("easy", "easy"),
                    ("medium", "medium"),
                    ("hard", "hard"),
                    ("expert", "expert"),
                ],
                default="easy",
                max_length=250,
            ),
        ),
    ]
