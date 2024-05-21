# Generated by Django 4.2.11 on 2024-05-21 18:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0019_forum_category"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="document",
            name="subjects",
        ),
        migrations.AddField(
            model_name="document",
            name="subject",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="subject_documents",
                to="app.subject",
            ),
        ),
    ]
