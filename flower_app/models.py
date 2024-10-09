from django.db import models


class Flower(models.Model):
    name = models.CharField(max_length=100, unique=True)
    x_position = models.IntegerField()
    y_position = models.IntegerField()
    start_date = models.PositiveIntegerField()
    end_date = models.PositiveIntegerField()
    image_url = models.URLField(max_length=200)  # Change to URLField

    def __str__(self):
        return self.name
