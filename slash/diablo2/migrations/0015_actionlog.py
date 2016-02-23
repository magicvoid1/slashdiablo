# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-09 14:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('diablo2', '0014_auto_20160206_0050'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActionLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(help_text='Which action was done', max_length=20)),
                ('target', models.CharField(help_text='Target of action', max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True, help_text='When the action was preformed')),
                ('user', models.ForeignKey(help_text='User who performed the action', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Action Log',
            },
        ),
    ]