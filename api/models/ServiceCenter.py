from django.db.models import CharField
from django.utils.translation import gettext_lazy as _

CENTER_CHOICES = (
    ('1', _('Alabama')),
    ('2', _('Arizona')),
    ('3', _('Arkansas')),
    ('4', _('Northern California')),
    ('5', _('Central California')),
    ('6', _('Southern California')),
    ('7', _('Colorado')),
    ('8', _('Connecticut')),
    ('9', _('Wisconsin')),
    ('10', _('Texas')),
)

class ServiceCenterField(CharField):
    """
    A model field that stores the two-digit Region number in the database.
    """

    description = _("Service Center (two digits)")

    def __init__(self, *args, **kwargs):
        kwargs['choices'] = CENTER_CHOICES
        kwargs['max_length'] = 2
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs['choices']
        return name, path, args, kwargs