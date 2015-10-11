# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_auto_20150926_2248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='line_total',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='line_item_total',
            field=models.DecimalField(decimal_places=2, default=19.99, max_digits=10),
            preserve_default=False,
        ),
    ]
