from django.contrib import admin # type: ignore
from .models import Players,TeamStanding

# Register your models here.
class PlayersAdmin(admin.ModelAdmin):
    list_display='name','position','jersey_no','mathch','goal','yellowcard','redcard',

class StandingAdmin(admin.ModelAdmin):
    list_display= 'team_name', 'matches_played', 'wins', 'draws', 'loss'

admin.site.register(Players,PlayersAdmin)

admin.site.register(TeamStanding,StandingAdmin)

