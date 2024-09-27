from django.db import models


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Sensors(models.Model):

    device_id = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=100)
    lat = models.FloatField()
    lon = models.FloatField()
    status = models.BooleanField(default=True)  # True = Active, False = Inactive
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.device_id


class SensorData(models.Model):

    sensor_id = models.ForeignKey(Sensors, on_delete=models.CASCADE)
    water_level = models.FloatField()
    rain_fall = models.FloatField()
    recorded_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sensor.name
