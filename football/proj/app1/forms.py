from django import forms # type: ignore
from .models import Players,TeamStanding

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Players
        fields = '__all__'


class TeamStandingForm(forms.ModelForm):
    class Meta:
        model = TeamStanding
        fields = ['team_name', 'matches_played', 'wins', 'draws', 'loss','points']