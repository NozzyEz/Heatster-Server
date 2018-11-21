from django.db import models
""" This file is for the models that are used to create and manipulate tables in our database,
this gives us a much better interface for doing queries """

# Model for the Weekdays
class Weekday(models.Model):
    class Meta:
        db_table = 'heatster_weekdays'

    name = models.CharField(max_length=255)

    object = models.Manager()


# Model for the Rooms
class Room(models.Model):
    class Meta:
        db_table = 'heatster_rooms'

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    
    object = models.Manager()


# Model for Valves
class Valve(models.Model):
    class Meta:
        db_table = 'heatster_valves'

    room_id = models.IntegerField()
    current_temp = models.FloatField()

    object = models.Manager()


# Model for Schedules
class Schedule(models.Model):
    class Meta:
        db_table = 'heatster_schedules'

    room_id = models.IntegerField()
    weekday_id = models.IntegerField()
    temperature = models.CharField(max_length=255)

    object = models.Manager()


# Model for Records
class Record(models.Model):
    class Meta:
        db_table = 'heatster_records'

    room_id = models.IntegerField()
    temperature = models.FloatField()
    time = models.DateTimeField()

    object = models.Manager()


# Model for Vacations
class Vacation(models.Model):
    class Meta:
        db_table = 'heatster_vacations'
    
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    object = models.Manager()


# Model for Settings
class Setting(models.Model):
    class Meta:
        db_table = 'heatster_settings'

    vacation_temp = models.IntegerField()
    sleep_temp = models.IntegerField()
    sleep_start = models.TimeField()
    sleep_end = models.TimeField()
    
    object = models.Manager()
