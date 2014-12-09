# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='admin_comments',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tag',
            name='events',
            field=models.ManyToManyField(related_name='tags', to='website.Event'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tag',
            name='users',
            field=models.ManyToManyField(related_name='tags', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
