# Generated by Django 2.1.3 on 2018-11-17 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('heatster', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Records',
            new_name='Record',
        ),
        migrations.RenameModel(
            old_name='Rooms',
            new_name='Room',
        ),
        migrations.RenameModel(
            old_name='Schedules',
            new_name='Schedule',
        ),
        migrations.RenameModel(
            old_name='Settings',
            new_name='Setting',
        ),
        migrations.RenameModel(
            old_name='Vacations',
            new_name='Vacation',
        ),
        migrations.RenameModel(
            old_name='Valves',
            new_name='Valve',
        ),
        migrations.RenameModel(
            old_name='Weekdays',
            new_name='Weekday',
        ),
    ]
