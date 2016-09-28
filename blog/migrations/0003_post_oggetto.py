# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_sesso'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='oggetto',
            field=models.TextField(default='Vuoto'),
            preserve_default=False,
        ),
    ]
