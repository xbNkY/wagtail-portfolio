# Generated by Django 5.0.9 on 2024-10-24 11:47

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0002_flexpage_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexpage',
            name='content',
            field=wagtail.fields.StreamField([('embed_video', 1)], blank=True, block_lookup={0: ('wagtail.blocks.URLBlock', (), {'help_text': 'Add youtube video URL', 'required': True}), 1: ('wagtail.blocks.StructBlock', [[('video_url', 0)]], {})}, null=True),
        ),
    ]
