from django.contrib.auth import get_user_model
from api.models.service.Technician import Technician
def get_sentinel_user():
    return get_user_model().objects.get_or_create(username="deleted")[0]

def get_sentinel_tech():
    return Technician.objects.get_or_create(firstName="deleted",active=False)