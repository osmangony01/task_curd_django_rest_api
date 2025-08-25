from django.db import models
from datetime import date
from django.utils import timezone

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField(default=date.today)
    status = models.CharField(max_length=30, blank=True, null=True)
    estimated_time = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
