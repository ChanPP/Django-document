from django.db import models


# Create your models here.

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(
        max_length=100,
        blank=True,
    )


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateTimeField(
        blank=True,
        null=True,
    )
    num_stars = models.IntegerField()


class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Mddium'),
        ('L', 'Large'),
    )

    name = models.CharField(max_length=50)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)

    def __str__(self):
        return '{name} (PK: {pk}, 셔츠 사이즈{shirt_size}'.format(
            name=self.name,
            pk=self.pk,
            shirt_size=self.shirt_size,
        )
