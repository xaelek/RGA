import re
import string

from datetime import datetime

from django.db import models
from django.conf import settings

class BaseModel(models.Model):
	""" The Basic Model Everything Extends, gives us some fun methods and properties"""

	created_date = models.DateTimeField(auto_now_add=True)
	update_date = models.DateTimeField(auto_now=True)
	name = models.TextField()

	class Meta:
		abstract = True

	def getIcon(self):
		iconPath = (settings.IMAGE_PATH + 
					self.__class__.__name__.lower() + "s" + "/" + re.sub(r'[^\w\s]', '', self.name) + 
					settings.IMAGE_EXTENSION)
		return iconPath
