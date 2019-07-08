from django.shortcuts import render
from team.models import *
from django.views.decorators.cache import cache_page

@cache_page(60 * 15)
def index_team(request):
    teams = Teams.objects.all()
    text_teams = TextTeam.objects.all()
    return render(request, "page/team.html", {"teams": teams, "text_teams": text_teams, })