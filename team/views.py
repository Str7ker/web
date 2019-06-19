from django.shortcuts import render
from index.models import *

def index_team(request):
    teams = Team.objects.all()
    text_teams = TextTeam.objects.all()
    logos = Logo.objects.all()
    return render(request, "page/team.html", {"teams": teams, "text_teams": text_teams, "logos": logos})