# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodFest',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('order', models.IntegerField()),
                ('desc', models.CharField(max_length=200, blank=True, null=True)),
                ('link', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='adminuploads/sponsors/')),
            ],
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('order', models.IntegerField()),
                ('desc', models.CharField(max_length=200, blank=True, null=True)),
                ('link', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='adminuploads/sponsors/')),
                ('types', models.CharField(max_length=100, choices=[('Our Sponsors', 'Our Sponsors'), ('Our Media Partners', 'Our Media Partners'), ('Our Associations', 'Our Associations')])),
            ],
        ),
    ]
