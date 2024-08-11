from django.db import models
from django.contrib.auth.models import User

# Client model to store customer information
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user.username

# Staff model to store information about salon staff
class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=50)
    experience = models.PositiveIntegerField(help_text="Years of experience")

    def __str__(self):
        return f"{self.user.username} - {self.position}"

# Service model to store different services offered by the salon
class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.DurationField(help_text="Duration of service in HH:MM:SS format")

    def __str__(self):
        return self.name

# Appointment model to store appointment details
class Appointment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True, blank=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.client.user.username} - {self.service.name} on {self.appointment_date} at {self.appointment_time}"

    class Meta:
        unique_together = ('staff', 'appointment_date', 'appointment_time')
