# Generated by Django 2.2.6 on 2020-01-05 15:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('coupon', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 9, 15, 44, 51, 852103, tzinfo=utc)),
        ),
    ]
