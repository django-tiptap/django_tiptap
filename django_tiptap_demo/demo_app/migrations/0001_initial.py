# Generated by Django 3.2 on 2021-04-19 14:21

from django.db import migrations, models

import django_tiptap.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Note",
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
                ("content", django_tiptap.fields.TipTapTextField()),
            ],
        ),
    ]
