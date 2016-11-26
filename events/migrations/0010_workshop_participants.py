# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0009_auto_20161120_1917'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workshop_Participants',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('workshop', models.ForeignKey(to='events.Workshop', related_name='workshop')),
                ('workshop_part', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='workshop_participating')),
            ],
        ),
    ]
