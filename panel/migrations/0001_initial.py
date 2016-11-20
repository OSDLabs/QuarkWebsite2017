# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=10)),
                ('institute', models.CharField(max_length=120)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('N', "Don't wish to reveal")], max_length=1)),
                ('dob', models.DateField(auto_now_add=True)),
                ('year', models.CharField(choices=[('U1', 'Undergraduate 1st year'), ('U2', 'Undergraduate 2nd year'), ('U3', 'Undergraduate 3rd year'), ('U4', 'Undergraduate 4th year'), ('P1', 'Postgraduate 1st year'), ('P2', 'Postgraduate 2nd year'), ('SS', 'Schooling'), ('PH', 'PhD.')], max_length=2)),
                ('updatedtime', models.DateTimeField(auto_now=True)),
                ('settime', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
