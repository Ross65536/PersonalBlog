from .models import Person
import os

curr_username = os.environ['P_USERNAME']
def get_person():
    return Person.objects.filter(username=curr_username).first()

# RESUME
RESUME_PDF_URL = "https://cpd.org.au/wp-content/uploads/2014/11/placeholder.pdf"
