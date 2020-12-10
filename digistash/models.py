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
    name = models.CharField(max_length=100)
    evolution = models.CharField(max_length=100, blank=True)
    meat_to_evolve = models.IntegerField(default=0)
    money_to_evolve = models.IntegerField(default=0)
    image_name = models.CharField(max_length=100)

