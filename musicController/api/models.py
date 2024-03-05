from django.db import models
import string
import random

def generate_unique_code():
    length = 6

    while(True):
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Room.objects.filter(code = code).count() == 0: #gives all room objects. Returns a count of the list of all objects that meet the criteria of code = code. 
            break

    return code


# Create your models here.
class Room(models.Model):
    code = models.CharField(max_length=8, default="", unique=True)
    host = models.CharField(max_length=50, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)

