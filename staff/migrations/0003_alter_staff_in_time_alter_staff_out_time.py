# Generated by Django 4.1.3 on 2023-02-28 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_staff_current_status_staff_in_time_staff_out_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='in_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='out_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
