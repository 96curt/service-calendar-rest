from django.db.models import CharField, Model, ManyToManyField
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

class ServiceCodeField(CharField):
    """
    A model field that stores the two-digit service codes in the database.
    """

    description = _("Service Center (two digits)")

    def __init__(self, *args, **kwargs):
        kwargs['choices'] = choices.SERVICE_CODES
        kwargs['max_length'] = 2
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs['choices']
        return name, path, args, kwargs

class WarrantyCodeField(CharField):
    """
    A model field that stores the two-digit Warranty code in the database.
    """

    description = _("Warrenty Code (1 digit)")

    def __init__(self, *args, **kwargs):
        kwargs['choices'] = choices.WARRANTY_CODES
        kwargs['max_length'] = 1
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs['choices']
        return name, path, args, kwargs

class CommentTypeField(CharField):
    """
    A model field that stores the Comment type code in the database.
    """

    description = _("Comment Type Code (1 digit)")

    def __init__(self, *args, **kwargs):
        kwargs['choices'] = choices.COMMENT_TYPE
        kwargs['max_length'] = 1
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs['choices']
        return name, path, args, kwargs

class StatusCodeField(CharField):
    """
    A model field that stores the Service Status Code in the database.
    """

    description = _("Status Code (1 digit)")

    def __init__(self, *args, **kwargs):
        kwargs['choices'] = choices.STATUS_CODES
        kwargs['max_length'] = 1
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs['choices']
        return name, path, args, kwargs


