# Generated by Django 5.0.7 on 2024-07-23 16:40

import taggit.managers
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_alter_post_slug"),
        (
            "taggit",
            "0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="tags",
            field=taggit.managers.TaggableManager(
                blank=True,
                help_text="A comma-separated list of tags.",
                through="taggit.TaggedItem",
                to="taggit.Tag",
                verbose_name="Tags",
            ),
        ),
    ]