from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext, loader

from portal.models import Game, Achievement, Console

def mainview(request):
    return HttpResponseRedirect('/rga')

def rga(request):
	return render(request, 'public/rga.html')

def games(request):
	gameList = Game.objects.order_by('name')
	return render(request, 'public/games.html', {'gameList': gameList})

def gameDetails(request, game_id):
	game = Game.objects.get(id=game_id)
	achievementsList = Achievement.objects.filter(game=game).order_by('name')
	return render(request, 'public/gameDetails.html', {
		'game': game,
		'achievementsList': achievementsList,
	})

def achievements(request):
	return render(request, 'public/achievements.html')

def achievementDetails(request, achievement_id):
	achievement = Achievement.objects.get(id=achievement_id)
	return render(request, 'public/achievementDetails.html', {
		'achievement': achievement
	})

def consoles(request):
	consoleList = Console.objects.order_by('name')
	return render(request, 'public/consoles.html', {'consoleList': consoleList})

def consoleDetails(request, console_id):
	console = Console.objects.get(id=console_id)
	gameList = Game.objects.filter(console=console).order_by('name')
	return render(request, 'public/consoleDetails.html', {
		'console': console, 
		'gameList': gameList
	})