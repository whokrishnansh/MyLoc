# Generated by Django 5.0.3 on 2024-03-30 06:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0010_alter_customer_profile_alter_upload_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='total_memory',
            field=models.IntegerField(default=10000000),
        ),
        migrations.AlterField(
            model_name='upload',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 3, 30, 12, 3, 13, 303536)),
        ),
    ]
