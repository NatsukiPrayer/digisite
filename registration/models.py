from django.db import models
from django.contrib.auth.models import User
from digistash.models import Digimon

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    digimons = models.ManyToManyField(Digimon, blank=True, null=True)
    money = models.IntegerField(default=999)
    meat = models.IntegerField(default=999)
    @classmethod
    def create(cls, user, money, meat):
        prof = cls(user=user, money=money, meat=meat)
        # do something with the book
        return prof
    def check_digi(self):
        print(self.digimons)
        return self.digimons is None