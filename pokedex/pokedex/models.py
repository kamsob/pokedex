from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    move1 = models.CharField(max_length=30, blank=True, null=True)
    move2 = models.CharField(max_length=30, blank=True, null=True)
    move3 = models.CharField(max_length=30, blank=True, null=True)
    move4 = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.name