from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class Digimon(models.Model):
    TYPES = [('Baby Dragon', 'Baby dragon'), ('Dragon', 'Dragon'), ('Mythical Dragon', 'Mythical Dragon'),
             ('Holy Knight', 'Holy Knight'), ('Lesser', 'Lesser'), ('Reptile', 'Reptile'),
             ('Dark Dragon', 'Dark Dragon'), ('Cyborg', 'Cyborg'), ('Beast', 'Beast'),
             ('Insect', 'Insect'), ('Mammal', 'Mammal'), ]
    ATTRIBUTES = [('Vaccine', 'Vaccine'), ('Data', 'Data'), ('Virus', 'Virus'),
                  ('Free', 'Free'), ]
    LEVELS = [('In-Training', 'In-Training'), ('Rookie', 'Rookie'),
              ('Champion', 'Champion'), ('Ultimate', 'Ultimate'),
              ('Mega', 'Mega'), ]
    name = models.CharField(max_length=100)
    level = models.CharField(choices=LEVELS, max_length=11, default=LEVELS[0])
    type = models.CharField(choices=TYPES, max_length=16, default=TYPES[0])
    attribute = models.CharField(choices=ATTRIBUTES, max_length=9, default=ATTRIBUTES[0])
    evolution = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=2000, default='Some digimon')
    Attacks = models.CharField(max_length=200, default='Some attack')
    meat_to_evolve = models.IntegerField(default=0)
    money_to_evolve = models.IntegerField(default=0)
    image_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

