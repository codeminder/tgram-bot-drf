from django.db import models

class Advise(models.Model):
    
    """
    Represents an advice entry in the system.

    Fields:
        text (str): The advice text, limited to 255 characters.
    """
    
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text
