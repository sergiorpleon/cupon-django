# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oferta', '0003_auto_20180808_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='oferta',
            name='nombre',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
