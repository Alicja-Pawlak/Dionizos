from django.db import models


# Create your models here.
class Color(models.Model):
    color = models.CharField(max_length=32,
                              unique=True)
    
    class Meta:
        ordering = ["color",]
        verbose_name = "color"
        verbose_name_plural = "colors"
    
    def __str__(self):
        return self.color
    

class Taste(models.Model):
    taste = models.CharField(max_length=32,
                              unique=True)
    class Meta:
        ordering = ["taste",]
        verbose_name = "taste"
        verbose_name_plural = "tastes"
    
    def __str__(self):
        return self.taste
    
class Wine(models.Model):
    name = models.TextField(max_length=32,
                              unique=True,
                              verbose_name="name")

    price = models.DecimalField(max_digits=6,
                               decimal_places=2)


    color = models.ForeignKey(Color,
                                 null=True,
                                 blank=True,
                                 on_delete=models.PROTECT,
                                 verbose_name="color",
                                 related_name="wines")


    taste = models.ForeignKey(Taste,
                                 null=True,
                                 blank=True,
                                 on_delete=models.PROTECT,
                                 verbose_name="taste",
                                 related_name="wines")
    
    descriptions = models.TextField(default="",
                               blank=True,
                               verbose_name="opis")

    pictures = models.ImageField(upload_to = 'Wystawowe/')

    def __str__(self):
       return self.name


class Comment(models.Model):

    
   wine = models.ForeignKey(Wine,
                      on_delete=models.CASCADE,
                      related_name='comments',)

   nickname  = models.CharField(max_length=32,
                         verbose_name="Imię",
                         null=True)

   description = models.TextField(default="",
                               blank=True,
                               verbose_name="Opinia",
                               null=True)
   def __str__(self):
        return 'Comment {} by {}'.format(self.description, self.nickname)

class WineImage(models.Model):
   wine = models.ForeignKey(Wine,
                      on_delete=models.CASCADE,
                      related_name='wine',)

   wineimage = models.ImageField()

   def __str__(self):
       return self.wine.name
