# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20161002_1715'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodFest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.IntegerField()),
                ('desc', models.CharField(null=True, max_length=200, blank=True)),
                ('link', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='adminuploads/sponsors/')),
            ],
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.IntegerField()),
                ('desc', models.CharField(null=True, max_length=200, blank=True)),
                ('link', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='adminuploads/sponsors/')),
                ('types', models.CharField(choices=[('Our Sponsors', 'Our Sponsors'), ('Our Media Partners', 'Our Media Partners'), ('Our Associations', 'Our Associations')], max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='event',
            old_name='event_category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='eventDate',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='event_desc',
            new_name='desc',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='eventpic',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='eventName',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='eventRules',
            new_name='rules',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='event_type',
            new_name='types',
        ),
        migrations.RenameField(
            model_name='rounds',
            old_name='roundDay',
            new_name='day',
        ),
        migrations.RenameField(
            model_name='rounds',
            old_name='roundLocation',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='rounds',
            old_name='roundTime',
            new_name='time',
        ),
        migrations.RenameField(
            model_name='rounds',
            old_name='roundTitle',
            new_name='title',
        ),
    ]
