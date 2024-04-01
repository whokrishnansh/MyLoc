# Generated by Django 5.0.3 on 2024-03-28 13:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0008_auto_20190308_0923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='age',
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='customer',
            name='total_memory',
            field=models.IntegerField(default=5242880),
        ),
        migrations.AlterField(
            model_name='upload',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 3, 28, 18, 42, 37, 322147)),
        ),
    ]
