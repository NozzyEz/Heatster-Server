# P3_server

This is the project for our django webserver for the Heatster solution.

there is no frontend, other than for the REST api, which can be used instead
 of Insomnia or a commandline/terminal tool.

To use the API you first need a token, to get this you need the username and password of the
 user/valve, and do a POST request to the url: 
api/auth/

ex.
http POST http://192.168.0.80:8000/api/auth/ username="user" password="randomPassword"

this will return a token that can be used to do the next HTTP requests that can be done.

list/create views:
Allows: GET, POST requests
rooms/
valves/
schedules/
records/


request type: GET
[    
    {
        "current_temp": 0.0,
        "id": 1,
        "name" : "name_of_room",
        "set_temp: 0.0
    },
    {
        "current_temp": 0.0,
        "id": 2,
        "name" : "name_of_room",
        "set_temp: 0.0
    }
]
retrieve, update and destroy views: (where x is the id of the row)
Allows: GET, PUT, DESTROY
weekdays/x/
rooms/x/
valves/x/
schedules/x/
records/x/
vacations/x/
settings/x/

ex.
http GET http://192.168.0.80:8000/api/rooms/ "Authoriztion: Token <sometokenhere>" 