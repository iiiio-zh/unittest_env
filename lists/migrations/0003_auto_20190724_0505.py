# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-24 05:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lists', '0002_list_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='shared_with',
            field=models.ManyToManyField(related_name='shared_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='list',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='list_owner', to=settings.AUTH_USER_MODEL),
        ),
    ]
