# Generated by Django 2.1.3 on 2018-12-05 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('heatster', '0007_auto_20181205_2118'),
    ]

    operations = [
        migrations.RenameField(
            model_name='valve',
            old_name='room_id',
            new_name='room',
        ),
    ]