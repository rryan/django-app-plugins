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
            name='Plugin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(help_text='The label for the plugin point.', unique=True, max_length=255)),
                ('index', models.IntegerField(default=0)),
                ('registered', models.BooleanField(default=False, help_text='is this a registered plugin?')),
                ('status', models.SmallIntegerField(default=0, choices=[(0, 'Enabled'), (1, 'Disabled'), (2, 'Removed')])),
                ('required', models.BooleanField(default=False, help_text='users can not remove this plugin.')),
                ('template', models.TextField(help_text='template to load for the plugin.')),
            ],
            options={
                'ordering': ('point', 'index', 'id'),
            },
        ),
        migrations.CreateModel(
            name='PluginPoint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(help_text='The label for the plugin point.', unique=True, max_length=255)),
                ('index', models.IntegerField(default=0)),
                ('registered', models.BooleanField(default=False, help_text='is this a registered plugin point with a library entry?')),
                ('status', models.SmallIntegerField(default=0, choices=[(0, 'Enabled'), (1, 'Disabled'), (2, 'Removed')])),
            ],
            options={
                'ordering': ('index', 'id'),
            },
        ),
        migrations.CreateModel(
            name='UserPluginPreference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('visible', models.BooleanField(default=True)),
                ('index', models.IntegerField(default=0)),
                ('plugin', models.ForeignKey(to='app_plugins.Plugin')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('plugin', 'user', 'index', 'id'),
            },
        ),
        migrations.AddField(
            model_name='plugin',
            name='point',
            field=models.ForeignKey(to='app_plugins.PluginPoint'),
        ),
        migrations.AlterUniqueTogether(
            name='userpluginpreference',
            unique_together=set([('user', 'plugin')]),
        ),
        migrations.AlterOrderWithRespectTo(
            name='userpluginpreference',
            order_with_respect_to='plugin',
        ),
        migrations.AlterOrderWithRespectTo(
            name='plugin',
            order_with_respect_to='point',
        ),
    ]
