from datetime import datetime
from django.db import models
from django.conf import settings
from portal.models.base import BaseModel

class Console(BaseModel):
	
	description = models.TextField()
	
	class Meta:
		app_label='portal'

	def __str__(self):
		return self.name