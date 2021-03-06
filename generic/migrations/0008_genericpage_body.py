# Generated by Django 3.2.8 on 2021-10-09 18:29

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('generic', '0007_genericpage_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='genericpage',
            name='body',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('paragraph', wagtail.core.blocks.RichTextBlock())], null=True),
        ),
    ]
