# Generated by Django 3.2 on 2021-10-11 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("demo_app", "0003_auto_20210630_1246"),
    ]

    operations = [
        migrations.AlterField(
            model_name="note",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]