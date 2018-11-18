# Generated by Django 2.1.3 on 2018-11-17 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('heatster', '0003_auto_20181117_1126'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='record',
            table='heatster_records',
        ),
        migrations.AlterModelTable(
            name='room',
            table='heatster_rooms',
        ),
        migrations.AlterModelTable(
            name='schedule',
            table='heatster_schedules',
        ),
        migrations.AlterModelTable(
            name='setting',
            table='heatster_settings',
        ),
        migrations.AlterModelTable(
            name='vacation',
            table='heatster_vacations',
        ),
        migrations.AlterModelTable(
            name='valve',
            table='heatster_valves',
        ),
        migrations.AlterModelTable(
            name='weekday',
            table='heatster_weekdays',
        ),
    ]
