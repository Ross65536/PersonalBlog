from .models import Person
import os

curr_username = os.environ['P_USERNAME']
def get_person():
    return Person.objects.filter(username=curr_username).first()
