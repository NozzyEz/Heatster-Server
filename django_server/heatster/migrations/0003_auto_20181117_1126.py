# Generated by Django 2.1.3 on 2018-11-17 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('heatster', '0002_auto_20181117_1015'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='setting',
            table='settings',
        ),
        migrations.AlterModelTable(
            name='vacation',
            table='vacations',
        ),
    ]
