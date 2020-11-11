from django.db import models

# Create your models here.
class course(models.Model):
    name=models.CharField(max_length=64)
    description=models.TextField()
    durations=models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.durations})"
