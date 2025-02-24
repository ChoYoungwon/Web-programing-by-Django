# Generated by Django 5.0.7 on 2024-07-20 02:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(
                allow_unicode=True,
                help_text="one word for title alias.",
                unique=True,
                verbose_name="SLUG",
            ),
        ),
    ]
