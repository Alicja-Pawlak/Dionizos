from django.db import models


# Create your models here.

class Wines(models.Model):
    name = models.TextField(max_length=32,
                              unique=True,
                              verbose_name="name")

    price = models.DecimalField(max_digits=6,
                               decimal_places=2)

    RED ="r"
    WHITE = "w"
    PINK = "p"

    COLOURS = [(RED, "czerwone"),
               (WHITE, "białe"),
               (PINK, "różowe")]

    Color = models.CharField(max_length=1,
                              choices=COLOURS,)

    SWEET = "s"
    SEMISWEET = "se"
    DRY = "d"
    SEMIDRY = "sd"

    TASTE = [(SWEET, "slodkie"),
             (SEMISWEET, "polslodkie"),
             (DRY, "wytrawne"),
             (SEMIDRY, "połwytrawne")]

    taste = models.CharField(max_length=2,
                              choices=TASTE,)
    
    descriptions = models.TextField(default="",
                               blank=True,
                               verbose_name="opis")

    picture = models.TextField(default="",
                               blank=True,
                               verbose_name="picture")

    def __str__(self):
        return self.name