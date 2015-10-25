# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0008_auto_20151025_1647'),
        ('orders', '0003_useraddress'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('shipping_total_price', models.DecimalField(max_digits=50, decimal_places=2, default=5.99)),
                ('order_total', models.DecimalField(max_digits=50, decimal_places=2)),
                ('billing_address', models.ForeignKey(to='orders.UserAddress', related_name='billing_address')),
                ('cart', models.ForeignKey(to='carts.Cart')),
                ('shipping_address', models.ForeignKey(to='orders.UserAddress', related_name='shipping_address')),
                ('user', models.ForeignKey(to='orders.UserCheckout')),
            ],
        ),
    ]
