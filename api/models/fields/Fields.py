from django.db.models import CharField
from api.models.fields import choices
from django.utils.translation import gettext_lazy as _

class RegionField(CharField):
    """
    A model field that stores the two-digit Region number in the database.
    """

    description = _("Region (two digits)")

    def __init__(self, *args, **kwargs):
        kwargs['choices'] = choices.REGION_CHOICES
        kwargs['max_length'] = 2
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs['choices']
        return name, path, args, kwargs

class ServiceCenterField(CharField):
    """
    A model field that stores the two-digit Service Center number in the database.
    """

    description = _("Service Center (two digits)")

    def __init__(self, *args, **kwargs):
        kwargs['choices'] = choices.CENTER_CHOICES
        kwargs['max_length'] = 2
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs['choices']
        return name, path, args, kwargs

class TerritoryManagerField(CharField):
    """
    A model field that stores the two-digit Territory Manager number in the database.
    """

    description = _("Service Center (two digits)")

    def __init__(self, *args, **kwargs):
        kwargs['choices'] = choices.MANAGER_CHOICES
        kwargs['max_length'] = 2
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs['choices']
        return name, path, args, kwargs