from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Valve, Room

@receiver(post_save, sender=Valve)
def room_temp_handler(sender, instance, **kwargs):
    ''' Listen for updates to the valve model, in order to set the average current temperature of
    all valves in a room, to the current temperature in that room '''
    # Find the valve that has been saved
    primary_valve = instance.id
    
    # Find the room that valve is in
    room_id = instance.room.id
    
    # Find the valves in that room and store their individual current_temperatures
    valve_objects = instance.room.valve.all()
    summed_temp = 0
    # Get the proper valves one by one
    for valve in valve_objects:
        # Look at it's current temperature and sum it up
        summed_temp += valve.current_temp

    # Calculate and average current temperature
    room_temp = summed_temp / len(valve_objects)
    
    # Store that average in the room's current_temperature
    for room in Room.object.filter(id=instance.room.id):
        room.current_temp = room_temp
        room.save()