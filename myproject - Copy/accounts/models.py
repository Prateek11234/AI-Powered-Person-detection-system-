from django.db import models

class Enrollment(models.Model):
    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female')], blank=True)
    date_of_birth = models.DateField(default='1900-01-01')  # Add a default value
    identification = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=100, blank=True)
    pincode = models.CharField(max_length=10, blank=True)
    additional_info = models.TextField(blank=True)

    def __str__(self):
        return self.full_name