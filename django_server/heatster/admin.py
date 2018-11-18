from django.contrib import admin
from .models import Weekday, Room, Valve, Schedule, Record, Vacation, Setting

admin.site.register(Weekday)
admin.site.register(Room)
admin.site.register(Valve)
admin.site.register(Schedule)
admin.site.register(Record)
admin.site.register(Vacation)
admin.site.register(Setting)
