# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0005_auto_20150929_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='tax_total',
            field=models.DecimalField(null=True, default=25.0, decimal_places=2, max_digits=50),
        ),
        migrations.AddField(
            model_name='cart',
            name='total',
            field=models.DecimalField(null=True, default=25.0, decimal_places=2, max_digits=50),
        ),
        migrations.AlterField(
            model_name='cart',
            name='subtotal',
            field=models.DecimalField(null=True, default=25.0, decimal_places=2, max_digits=50),
        ),
    ]
