# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-13 09:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_filer_teaser', '0003_auto_20160713_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filerteaser',
            name='image',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.FILER_IMAGE_MODEL, verbose_name='image'),
        ),
    ]