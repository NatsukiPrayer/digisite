from django.db import models
from django.contrib.auth.models import User
from digistash.models import Digimon

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    digimons = models.ManyToManyField(Digimon, blank=True)
    money = models.IntegerField(default=999)
    meat = models.IntegerField(default=999)
    haveV = models.BooleanField(default=False)
    haveG = models.BooleanField(default=False)
    haveT = models.BooleanField(default=False)
    @classmethod
    def create(cls, user, money, meat):
        prof = cls(user=user, money=money, meat=meat)
        # do something with the book
        return prof
    def check_digi(self):
        print(self.digimons)
        if self.digimons.all():
            return True
        else:
            return False
    def digi_list(self):
        out=[]
        for digimon in self.digimons.all():
            out.append(digimon.name)
        return out
    def __str__(self):
        return self.user.username