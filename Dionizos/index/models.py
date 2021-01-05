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

    color = models.CharField(max_length=1,
                              choices=COLOURS,
                              verbose_name="color")

    SWEET = "s"
    SEMISWEET = "se"
    DRY = "d"
    SEMIDRY = "sd"

    TASTE = [(SWEET, "słodkie"),
             (SEMISWEET, "półsłodkie"),
             (DRY, "wytrawne"),
             (SEMIDRY, "półwytrawne")]

    taste = models.CharField(max_length=2,
                              choices=TASTE,
                              verbose_name="taste")
    
    descriptions = models.TextField(default="",
                               blank=True,
                               verbose_name="opis")

    picture = models.TextField(default="",
                               blank=True,
                               verbose_name="picture")

    # te funkcje zwracają dobre nazwy 
    # (czerwone, a nie 'r', półsłodkie, a nie 'se') 
    def color_name(self):
        for name in self.COLOURS:
            if self.color == name[0]:
                return name[1]
        return "?"
        
    def taste_name(self):
        for name in self.TASTE:
            if self.taste == name[0]:
                return name[1]
        return "?"

    def __str__(self):
        return self.name

