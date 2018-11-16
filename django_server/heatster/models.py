from django.db import models


# Model for the Weekdays
class Weekdays(models.Model):
    name = models.CharField(max_length=255)


# Model for the Rooms
class Rooms(models.Model):
    name = models.CharField(max_length=255)


# Model for Valves
class Valves(models.Model):
    room_id = models.IntegerField()
    current_temp = models.FloatField()


# Model for Schedules
class Schedules(models.Model):
    room_id = models.IntegerField()
    weekday_id = models.IntegerField()
    temperature = models.CharField(max_length=255)


# Model for Records
class Records(models.Model):
    room_id = models.IntegerField()
    temperature = models.FloatField()
    time = models.DateTimeField()


# Model for Vacations
class Vacations(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()


# Model for Settings
class Settings(models.Model):
    vacation_temp = models.IntegerField()
    sleep_temp = models.IntegerField()
    sleep_start = models.TimeField()
    sleep_end = models.TimeField()
