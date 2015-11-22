from django.db import models
from apis.models import Api

class Endpoint(models.Model):
	HTTP_METHODS = (
		('GET','GET'),
		('POST','POST'),
		('PUT','PUT'),
		('DELETE','DELETE'),
	)

	def __unicode__(self):
		return method + ': ' + url
	url = models.URLField()
	api = models.ForeignKey(Api)
	method = models.CharField(choices=HTTP_METHODS, max_length=10, default='GET')	
	description = models.TextField(max_length=100)
