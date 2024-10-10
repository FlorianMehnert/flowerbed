from django.db import models


class Flower(models.Model):
    name = models.CharField(verbose_name='BLumenname', max_length=100, unique=True)
    x_position = models.IntegerField()
    y_position = models.IntegerField()
    start_date = models.PositiveIntegerField(verbose_name='Anfang Blühzeit')
    end_date = models.PositiveIntegerField(verbose_name='Ende Blühzeit')
    image_url = models.URLField(verbose_name='Bildlink', max_length=200)  # Change to URLField

    def __str__(self):
        return self.name
