# Generated by Django 2.1.3 on 2018-12-02 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heatster', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='hour',
        ),
        migrations.AlterField(
            model_name='schedule',
            name='temperature',
            field=models.CharField(max_length=255),
        ),
    ]