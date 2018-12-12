""" This is the serializers file, these exist to take data from the database models and convert 
it to JSON, and possibly, if necesarry, perform validations """
from rest_framework import serializers
from heatster.models import (Record, Room, Schedule, Setting, Vacation, Valve,
                             Weekday)


class WeekdaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Weekday
        fields = [
            'id',
            'name'
        ]

        read_only_fields = ['name']


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = [
            'id',
            'name',
            'current_temp',
            'set_temp',
            'valve'
        ]

        
class ValveSerializer(serializers.ModelSerializer):
    ''' Valve serializer which is used to validate and make sure that information is
    presented in the correct way inside of the JSON object being returned''' 
    class Meta:
        # Specify the model to use and the fields to expose to the HTTP request
        model = Valve
        fields = [
            'id',
            'current_temp',
            'room'
        ]
    
    # this method is used so that we only need the room_id when we POST or PATCH a valve,
    # but get the whole object when doing a GET
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['room'] = RoomSerializer(Room.object.get(id=data['room'])).data
        return data
                

class ScheduleSerializer(serializers.ModelSerializer):
    weekday = serializers.SlugRelatedField(queryset=Weekday.object.all(), slug_field='name')

    class Meta:
        model = Schedule
        fields = [
            'id',
            'room',
            'weekday',
            'temperature'
        ]


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = [
            'id',
            'room_id',
            'temperature',
            'time'
        ]


class VacationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacation
        fields = [
            'id',
            'start_date',
            'end_date'
        ]


class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setting
        fields = [
            'id',
            'vacation_temp',
            'sleep_temp',
            'sleep_start',
            'sleep_end'
        ]
