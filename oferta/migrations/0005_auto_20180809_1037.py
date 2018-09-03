# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oferta', '0004_oferta_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oferta',
            name='photo',
            field=models.ImageField(null=True, upload_to=b'photos/', blank=True),
            preserve_default=True,
        ),
    ]
