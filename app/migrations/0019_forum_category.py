# Generated by Django 4.2.11 on 2024-05-21 17:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0018_alter_like_content_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="forum",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="category_forums",
                to="app.category",
            ),
        ),
    ]