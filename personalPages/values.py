from .models import Person

def get_person():
    return Person.objects.first()

# RESUME
RESUME_PDF_URL = "https://cpd.org.au/wp-content/uploads/2014/11/placeholder.pdf"
