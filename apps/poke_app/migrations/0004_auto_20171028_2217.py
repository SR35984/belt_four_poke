# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-28 22:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poke_app', '0003_remove_poke_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poke',
            name='poked_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pokee', to='poke_app.User'),
        ),
        migrations.AlterField(
            model_name='poke',
            name='poker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poker', to='poke_app.User'),
        ),
    ]
