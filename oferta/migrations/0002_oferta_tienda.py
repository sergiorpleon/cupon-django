# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0001_initial'),
        ('oferta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='oferta',
            name='tienda',
            field=models.ForeignKey(to='tienda.Tienda'),
            preserve_default=True,
        ),
    ]
