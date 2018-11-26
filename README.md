# P3_server
**This documentation is still under construction**

This is the project for our django webserver for the Heatster solution.

*There is no frontend, other than for the REST api, which can be used instead of Insomnia or a 
commandline/terminal tool.*

## Creating a local copy
```
To create a local copy, you need to Install Python 3 and PostgreSQL first of all.
It is strongly advised to use a virtual enviornment.
<<<<<<< HEAD
Once in the virtual enviornment you need to install the following packages with pip: django, 
djangorestframework
Inside of your installed PostgreSQL server, you need to create a database and a user with the 
following information:
=======
Once in the virtual enviornment you need to install the following packages with pip: django, djangorestframework, psycopg2
Inside of your installed PostgreSQL server, you need to create a database and a user with the following information:
Database name:  p3_server
user:           p3_server
password:       Testing321
```

## Connecting to the Raspberry Pi
Open a terminal or a commandline tool and write:
```
ssh 192.168.0.80 -l pi
password: raspberry
cd git-repos/P3_server/django_server
source bin/activate
python3 manage.py runserver 192.168.0.80:8000
```



## Token Authentication
To use the API you first need a token, to get this you need the username and password of the
 user/valve, and do a POST request to the url: 
api/auth/

ex.
```
http POST http://192.168.0.80:8000/api/auth/ username="user" password="randomPassword"
```

this will return a token that can be used to do the HTTP requests that are possible within our API,
everything needs authorization.

## API calls
### list/create views:
Allows: **GET, POST** requests

rooms/
```
request type: GET
[    
    {
        "id": 1, (Int)
        "name" : "name_of_room", (String)
        "current_temp": 0.0, (Float)
        "set_temp: 0.0 (Float)
    },
    {
        "id": 2, (Int)
        "name" : "name_of_room", (String)
        "current_temp": 0.0, (Float)
        "set_temp: 0.0 (Float)
    }
]
```

valves/
```
request type: GET
[    
    {
        "id": 1, (Int)
        "room_id" : 1, (Int)
        "current_temp": 0.0, (Float)
        "set_temp: 0.0 (Float)
    },
    {
        "id": 2, (Int)
        "room_id" : 1, (Int)
        "current_temp": 0.0, (Float)
        "set_temp: 0.0 (Float)
    }
]
```

schedules/
```
request type: GET
[
    {
        "id": 1 (Int),
        "room_id": 1 (Int),
        "weekday_id": 1 (Int),
        "hour": 1 (Int),
        "temperature": 0.0 (Float)
    }
    {
        "id": 2 (Int),
        "room_id": 1 (Int),
        "weekday_id": 1 (Int),
        "hour": 2 (Int),
        "temperature": 0.0 (Float)
    }
]
```
In schedules you can also search for specific weekday by typing the following urL:
```
(replace x with a number between 1 and 7)
192.168.0.80/api/schedules?weekday=x
```

records/
```
[
    {
        "id": 1 (Int),
        "room_id": 1 (Int),
        "temperature": 21.5 (Float)
        "time": 2018-11-07 18:00:00.327+01 (Timestamp with timezone),
    }
    {
        "id": 2 (Int),
        "room_id": 2 (Int),
        "temperature": 17.5 (Float)
        "time": 2018-11-07 18:00:00.327+01 (Timestamp with timezone),
    }
]
```


### retrieve, update and destroy views: (where x is the id of the row)
Allows: **GET, PUT, DESTROY**

weekdays/x/ (This shouldn't be a RUD view, we only want to be able to read these values, not update or destroy
```
{
    "id": 1 (Int)
    "name": "Monday" (String *read-only field*)
}
```

rooms/x/
```
{
    "id": 1, (Int)
    "name" : "name_of_room", (String)
    "current_temp": 0.0, (Float)
    "set_temp: 0.0 (Float)
}
```

valves/x/
```
{
    "id": 1, (Int)
    "room_id" : 1, (Int)
    "current_temp": 0.0, (Float)
    "set_temp: 0.0 (Float)
}
```

schedules/x/
```
{
    "id": 1 (Int),
    "room_id": 1 (Int),
    "weekday_id": 1 (Int),
    "hour": 1 (Int),
    "temperature": 0.0 (Float)
}
```

records/x/
```
{
    "id": 1 (Int),
    "room_id": 1 (Int),
    "temperature": 21.5 (Float)
    "time": 2018-11-07 18:00:00.327+01 (Timestamp with time zone),
}
```

vacations/x/
```
{
    "id": 1 (Int),
    "start_date": 2018-11-07 18:00:00.327+01 (Timestamp with time zone),
    "end_date": 2018-11-14 18:00:00.327+01 (Timestamp with time zone)
}
```

settings/x/
```
{
    "id": 1 (Int),
    "vacation_temp": 12.0 (Float),
    "sleep_temp": 17.0 (Float),
    "sleep_start": 22:30:00+8 (Time with time zone),
    "sleep_end": 06:30:00+8 (Time with time zone)
}
```

ex.
```
http GET http://192.168.0.80:8000/api/rooms/ "Authorization: Token (token_id)" 
```
