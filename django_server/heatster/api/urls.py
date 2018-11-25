""" This is where API related urls go, so we can point to the REST  """
from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from rest_framework.authtoken import views

from .views import (
    RetrieveWeekdayView,
    ListRoomView, ListValveView, ListScheduleView, ListRecordView, 
    RudRoomView, RudValveView, RudScheduleView, RudVacationView, RudSettingView
)

urlpatterns = [
    path('auth/', views.obtain_auth_token, name='api-token-auth'),
    path('weekdays/<int:id>/', RetrieveWeekdayView.as_view(), name='api-weekdays'),
    path('rooms/', ListRoomView.as_view(), name='api-rooms-list'),
    path('rooms/<int:id>', RudRoomView.as_view(), name='api-room'),
    path('valves/', ListValveView.as_view(), name='api-valve-list'),
    path('valves/<int:id>', RudValveView.as_view(), name='api-valve'),
    path('schedules/', ListScheduleView.as_view(), name='api-schedules-list'),
    path('schedules/<int:id>', RudScheduleView.as_view(), name='api-schedules'),
    path('records/', ListRecordView.as_view(), name='api-records'),
    path('vacations/<int:id>', RudVacationView.as_view(), name='api-vacation'),
    path('settings/<int:id>', RudSettingView.as_view(), name='api-settings')
]
