from django.shortcuts import render
from index.models import *

def index_team(request):
    teams = Team.objects.all()
    textteams = TextTeam.objects.all()
    return render(request, "page/team.html", {"teams": teams, "textteam": textteams})