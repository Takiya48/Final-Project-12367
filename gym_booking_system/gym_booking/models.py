from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    booking_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    purpose = models.TextField()
    status = models.CharField(max_length=20, choices=[
        ('Pending', 'รออนุมัติ'),
        ('Approved', 'อนุมัติแล้ว'),
        ('Rejected', 'ไม่อนุมัติ'),
    ], default='Pending')

    def __str__(self):
        return f"{self.name} - {self.booking_date}"
