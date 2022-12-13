from django.db import models
from django.utils import timezone
from datetime import timedelta

class User(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.TextField()
    Email = models.EmailField()
    Password = models.TextField()
    DOB = models.DateField()
    Payment_Date = models.DateField(default = timezone.now() - timedelta(days=300))
    Batch = models.IntegerField(default = 0)

    def __str__ (self):
        return self.Name

