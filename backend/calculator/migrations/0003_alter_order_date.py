# Generated by Django 3.2.7 on 2021-09-26 21:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0002_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 9, 26, 21, 56, 2, 669567, tzinfo=utc)),
        ),
    ]
