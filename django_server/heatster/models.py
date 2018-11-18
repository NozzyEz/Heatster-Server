from django.db import models
""" This file is for the models that are used to create and manipulate tables in our database,
this gives us a much better interface for doing queries """

# Model for the Weekdays
class Weekday(models.Model):
    class Meta:
        db_table = 'heatster_weekdays'

    name = models.CharField(max_length=255)


# Model for the Rooms
class Room(models.Model):
    class Meta:
        db_table = 'heatster_rooms'

    name = models.CharField(max_length=255)


# Model for Valves
class Valve(models.Model):
    class Meta:
        db_table = 'heatster_valves'

    room_id = models.IntegerField()
    current_temp = models.FloatField()


# Model for Schedules
class Schedule(models.Model):
    class Meta:
        db_table = 'heatster_schedules'

    room_id = models.IntegerField()
    weekday_id = models.IntegerField()
    temperature = models.CharField(max_length=255)


# Model for Records
class Record(models.Model):
    class Meta:
        db_table = 'heatster_records'

    room_id = models.IntegerField()
    temperature = models.FloatField()
    time = models.DateTimeField()


# Model for Vacations
class Vacation(models.Model):
    class Meta:
        db_table = 'heatster_vacations'
    
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()


# Model for Settings
class Setting(models.Model):
    class Meta:
        db_table = 'heatster_settings'

    vacation_temp = models.IntegerField()
    sleep_temp = models.IntegerField()
    sleep_start = models.TimeField()
    sleep_end = models.TimeField()
