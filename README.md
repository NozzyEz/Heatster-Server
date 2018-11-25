# P3_server
**This documentation is still under construction**

This is the project for our django webserver for the Heatster solution.

*There is no frontend, other than for the REST api, which can be used instead of Insomnia or a commandline/terminal tool.*

## Creating a local copy
```
To create a local copy, you need to Install Python 3 and PostgreSQL first of all.
It is strongly advised to use a virtual enviornment
Once in the virtual enviornment you need to install the following packages with pip: django, djangorestframework
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

this will return a token that can be used to do the HTTP requests that are possible within our API, everything needs authorization.

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

records/


### retrieve, update and destroy views: (where x is the id of the row)
Allows: **GET, PUT, DESTROY**

weekdays/x/

rooms/x/

valves/x/

schedules/x/

records/x/

vacations/x/

settings/x/

ex.
```
http GET http://192.168.0.80:8000/api/rooms/ "Authorization: Token (token_id)" 
```
