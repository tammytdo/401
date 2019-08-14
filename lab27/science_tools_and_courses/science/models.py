from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Tool(models.Model):
    tool_name = models.CharField(max_length=256)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.tool_name

    class Meta:
        unique_together = ('tool_name', 'course')