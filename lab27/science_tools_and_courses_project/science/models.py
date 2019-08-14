from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

        
class Tool(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name