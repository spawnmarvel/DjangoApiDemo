from django.db import models

# Create your models here.

class Bag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return "{}".format(self.name)



class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    f_key_bag = models.ForeignKey(Bag, on_delete=models.CASCADE)

    def __str__(self):
        return "{}, {}".format(self.name, self.description)

