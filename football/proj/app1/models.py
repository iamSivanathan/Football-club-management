from django.db import models # type: ignore

# Create your models here.

class Players(models.Model):
    # image = models.ImageField(upload_to='players/', null=True, blank=True)
    name = models.CharField(max_length=30)    
    position = models.CharField(max_length=20,choices= [
        ('GK', 'Goalkeeper'),
        ('DEF', 'Defender'),
        ('MID', 'Midfielder'),
        ('FWD', 'Forward'),
    ])
    # club = models.ImageField(upload_to='players/', null=True, blank=True)    
    jersey_no = models.IntegerField()
    mathch = models.IntegerField()
    goal = models.IntegerField()
    yellowcard = models.IntegerField()
    redcard = models.IntegerField()

    def __str__(self):
        return self.name
    
class TeamStanding(models.Model):
    team_name = models.CharField(max_length=100, unique=True)
    matches_played = models.PositiveIntegerField(default=0)
    wins = models.PositiveIntegerField(default=0)
    draws = models.PositiveIntegerField(default=0)
    loss = models.PositiveIntegerField(default=0)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.team_name
    

