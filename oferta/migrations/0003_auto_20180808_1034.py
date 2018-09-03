# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oferta', '0002_oferta_tienda'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oferta',
            name='descuento',
            field=models.DecimalField(max_digits=5, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='oferta',
            name='precio',
            field=models.DecimalField(max_digits=5, decimal_places=2),
            preserve_default=True,
        ),
    ]
