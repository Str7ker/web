from django.shortcuts import render
from team.models import *

def index_team(request):
    teams = Teams.objects.all()
    text_teams = TextTeam.objects.all()
    return render(request, "page/team.html", {"teams": teams, "text_teams": text_teams, })