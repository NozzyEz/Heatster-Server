from rest_framework import generics, mixins
from .serializers import (
    WeekdaySerializer,
    RoomSerializer,
    ValveSerializer,
    ScheduleSerializer,
    RecordSerializer,
    VacationSerializer,
    SettingSerializer
)
from heatster.models import Weekday, Room, Valve, Schedule, Record, Vacation, Setting


class RetrieveWeekdayView(generics.RetrieveAPIView):
    """ View to get the current weekday based on the id """
    lookup_field = 'id'
    serializer_class = WeekdaySerializer
    
    def get_queryset(self):
        return Weekday.object.all()


class ListRoomView(mixins.CreateModelMixin, generics.ListAPIView):
    """ View to obtain a list of the rooms, can be used to create new rooms in the database """
    lookup_field = 'id'
    serializer_class = RoomSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_queryset(self):
        return Room.object.all()

class RudRoomView(generics.RetrieveUpdateDestroyAPIView):
    """ RUD view for the room model to be able to retrieve a single room, update it, or delete it
    if need be """
    lookup_field = 'id'
    serializer_class = RoomSerializer

    def get_queryset(self):
        return Room.object.all()


class ListValveView(mixins.CreateModelMixin, generics.ListAPIView):
    """ Get a listview of all valves in the system """
    lookup_field = 'id'
    serializer_class = ValveSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_queryset(self):
        return Valve.object.all()    


class RudValveView(generics.RetrieveUpdateDestroyAPIView):
    """ update valve settings """
    lookup_field = 'id'
    serializer_class = ValveSerializer

    def get_queryset(self):
        return Valve.object.all()


class ListScheduleView(mixins.CreateModelMixin, generics.ListAPIView):
    """ get a list of the schedules that have been set up, this might need a rethink """
    lookup_field = 'id'
    serializer_class = ScheduleSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_queryset(self):
        # We use a custom get queyset method as to allow searching functionality
        queryset = Schedule.object.all()
        weekday_id = self.request.query_params.get('weekday', None)
        if weekday_id is not None:
            queryset = queryset.filter(weekday_id=weekday_id)
        return queryset


class RudScheduleView(generics.RetrieveUpdateDestroyAPIView):
    """ view to manipulate a given schedule """
    lookup_field = 'id'
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        return Schedule.object.all()


class ListRecordView(mixins.CreateModelMixin, generics.ListAPIView):
    """ Get a list of all the recorded data, presumably for future features like machine 
    learning """
    lookup_field = 'id'
    serializer_class = RecordSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_queryset(self):
        return Record.object.all()


class ListVacationView(mixins.CreateModelMixin, generics.ListAPIView):
    """ Get a list of vacations """
    lookup_field = 'id'
    serializer_class = VacationSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_queryset(self):
        return Record.object.all()


class RudVacationView(generics.RetrieveUpdateDestroyAPIView):
    """ Set a vacation start and end time """
    lookup_field = 'id'
    serializer_class = VacationSerializer

    def get_queryset(self):
        return Vacation.object.all()


class RudSettingView(generics.RetrieveUpdateDestroyAPIView):
    """ Overall settings for the system, custom temperatures for vacation and sleep and control 
    start and end time for sleep """
    lookup_field = 'id'
    serializer_class = SettingSerializer

    def get_queryset(self):
        return Setting.object.all()
