# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ciudad', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oferta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=500)),
                ('condiciones', models.CharField(max_length=500)),
                ('photo', models.CharField(max_length=255)),
                ('precio', models.IntegerField()),
                ('descuento', models.IntegerField()),
                ('fecha_expiracion', models.DateField(null=True, blank=True)),
                ('fecha_publicacion', models.DateField(null=True, blank=True)),
                ('compra', models.IntegerField()),
                ('umbral', models.IntegerField()),
                ('revisada', models.IntegerField()),
                ('ciudad', models.ForeignKey(to='ciudad.Ciudad')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(null=True, blank=True)),
                ('oferta', models.ForeignKey(to='oferta.Oferta')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
