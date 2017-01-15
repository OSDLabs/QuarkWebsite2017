# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='quick',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=10)),
                ('institute', models.CharField(max_length=120)),
                ('gender', models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female'), ('N', "Don't wish to reveal")])),
                ('year', models.CharField(max_length=2, choices=[('U1', 'Undergraduate 1st year'), ('U2', 'Undergraduate 2nd year'), ('U3', 'Undergraduate 3rd year'), ('U4', 'Undergraduate 4th year'), ('P1', 'Postgraduate 1st year'), ('P2', 'Postgraduate 2nd year'), ('SS', 'Schooling'), ('PH', 'PhD.')])),
                ('panel_des', models.CharField(max_length=100)),
                ('panel_elixir', models.CharField(max_length=100)),
                ('panel_robo', models.CharField(max_length=100)),
                ('panel_prog', models.CharField(max_length=100)),
                ('panel_specials', models.CharField(max_length=100)),
                ('panel_init', models.CharField(max_length=100)),
                ('panel_elect', models.CharField(max_length=100)),
                ('panel_corporate', models.CharField(max_length=100)),
                ('workshop', models.CharField(max_length=100)),
            ],
        ),
    ]
