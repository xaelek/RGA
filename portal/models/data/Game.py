from datetime import datetime
from django.db import models
from portal.models.base import BaseModel
from portal.models.data.Console import Console

class Game(BaseModel):

	description = models.TextField()

	console = models.ForeignKey(Console)

	class Meta:
		app_label ='portal'

	def __str__(self):
		return self.name