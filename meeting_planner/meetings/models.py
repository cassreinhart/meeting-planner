from datetime import time
from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=50)
    floor_number = models.IntegerField()
    room_number = models.IntegerField()

    def __str__(self):
        return f"Room {self.name} on floor {self.floor_number} room {self.room_number}"

class Meeting(models.Model):
    title = models.CharField(max_length=200) #specify columns
    date = models.DateField()
    start_time = models.TimeField(default=time(9)) #defaults will auto fill in older rows that were made before these colmns
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE) #if room is deleted, all meetings will also be removed

    def __str__(self):
        return f"{self.title} at {self.start_time} on {self.date}"
