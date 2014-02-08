from django.contrib import admin
from portal.models.data.Achievement import Achievement
from portal.models.data.Game import Game
from portal.models.data.Console import Console

class DisplayAdmin(admin.ModelAdmin):
	list_display = ('name', 'description')

admin.site.register(Console, DisplayAdmin)
admin.site.register(Achievement, DisplayAdmin)
admin.site.register(Game, DisplayAdmin)