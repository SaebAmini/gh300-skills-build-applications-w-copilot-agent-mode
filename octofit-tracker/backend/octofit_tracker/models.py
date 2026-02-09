from django.db import models
from django.contrib.auth.models import User as DjangoUser

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=200)
    age = models.IntegerField(null=True, blank=True)
    fitness_level = models.CharField(max_length=50, blank=True)
    team_id = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'users'


class Team(models.Model):
    name = models.CharField(max_length=200)
    captain_id = models.CharField(max_length=100, null=True, blank=True)
    member_count = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'teams'


class Activity(models.Model):
    user_id = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    duration = models.IntegerField()  # in minutes
    distance = models.FloatField(null=True, blank=True)  # in km
    calories = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.type} - {self.duration} mins"
    
    class Meta:
        db_table = 'activities'
        verbose_name_plural = 'activities'


class Leaderboard(models.Model):
    user_id = models.CharField(max_length=100)
    user_name = models.CharField(max_length=200)
    team_id = models.CharField(max_length=100, null=True, blank=True)
    team_name = models.CharField(max_length=200, null=True, blank=True)
    total_points = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.user_name} - {self.total_points} points"
    
    class Meta:
        db_table = 'leaderboard'
        ordering = ['-total_points']


class Workout(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    difficulty = models.CharField(max_length=50)
    duration = models.IntegerField()  # in minutes
    type = models.CharField(max_length=100)
    calories_estimate = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'workouts'
