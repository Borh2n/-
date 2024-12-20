from django.db import models


class Field(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    field_type = models.CharField(max_length=50)  
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Booking(models.Model):
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.user_name} - {self.field.name} on {self.date}"
