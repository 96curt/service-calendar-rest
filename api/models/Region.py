from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=128)

    # One to Many relations: centers, cities, zipCode, sequence
    # Many to many relations: managers
    
    def __str__(self):
        return self.name