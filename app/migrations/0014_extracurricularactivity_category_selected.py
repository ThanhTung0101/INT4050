# Generated by Django 4.2.4 on 2024-05-04 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0013_subject_selected"),
    ]

    operations = [
        migrations.CreateModel(
            name="ExtracurricularActivity",
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
                ("selected", models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name="category",
            name="selected",
            field=models.BooleanField(default=False),
        ),
    ]
