from datetime import datetime
from django.db import models
from portal.models.base import BaseModel
from portal.models.data.Game import Game

class Achievement(BaseModel):

	score = models.IntegerField()

	description = models.TextField()

	game = models.ForeignKey(Game)

	class Meta:
		app_label ='portal'

	def __str__(self):
		return self.name