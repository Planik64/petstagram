from django.contrib.auth.models import User
from django.db import models


class Pet(models.Model):
    DOG = 'dog'
    CAT = 'cat'
    PARROT = 'parrot'
    UNKNOWN = 'unknown'

    PET_TYPES = (
        (DOG, 'Dog'),
        (CAT, 'Cat'),
        (PARROT, 'Parrot'),
        (UNKNOWN, 'Unknown'),
    )

    type = models.CharField(max_length=7, choices=PET_TYPES, default=UNKNOWN)
    name = models.CharField(max_length=10, blank=False)
    age = models.IntegerField(blank=False)
    description = models.TextField(blank=False)
    image = models.ImageField( upload_to='public/pets',
        )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}; {self.name}; {self.age}'


class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=30, default='no name', blank=False)
    text = models.TextField(blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)