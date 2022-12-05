from django.db import models

class WorkWeek(models.Model):
    monday = models.BooleanField(default=False)
    tuesday = models.BooleanField(default=False)
    wedesday = models.BooleanField(default=False)
    thursday = models.BooleanField(default=False)
    friday = models.BooleanField(default=False)
    saturday = models.BooleanField(default=False)
    sunday = models.BooleanField(default=False)
    def __str__(self) -> str:
        return  ( 'M' if self.monday else '') + \
                ( 'T' if self.tuesday else '') + \
                ( 'W' if self.wedesday else '' ) + \
                ( 'Th' if self.thursday else '' ) + \
                ( 'F' if self.friday else '' ) + \
                ( 'Sa' if self.saturday else '' ) + \
                ( 'Su' if self.sunday else '' )
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['monday', 'tuesday', 'wedesday', 'thursday', 'friday', 'saturday', 'sunday'], name='unique_weeks') 
        ]
        

def get_sentinel_workWeek():
    return WorkWeek.objects.get_or_create()