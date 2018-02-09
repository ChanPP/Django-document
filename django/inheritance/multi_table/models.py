from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):
        return f'place {self.name} | {self.address}'


class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)
    # nearby_places = models.ManyToManyField(Place, related_query_name='near_retaurant')

    def __str__(self):
        return f'Restaurant {self.serves_hot_dogs} | {self.serves_pizza}'
