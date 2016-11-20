# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_auto_20161106_2301'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('brochure', models.FileField(blank=True, upload_to='adminuploads/workshop/brochure/', null=True)),
                ('img', models.ImageField(blank=True, upload_to='adminuploads/workshop/poster/', null=True)),
                ('desc', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='event',
            name='date',
        ),
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.CharField(max_length=50, default='', choices=[('Design & Build', 'Design & Build'), ('Programmers Inc.', 'Programmers Inc.'), ('Electrify', 'Electrify'), ('Roboficial', 'Roboficial'), ('Elixir', 'Elixir'), ('Specials', 'Specials'), ('Corporate', 'Corporate'), ('Initiatives', 'Initiatives'), ('Cubing', 'Cubing'), ('Matka', 'Matka')]),
        ),
    ]
