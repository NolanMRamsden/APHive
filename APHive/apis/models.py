from django.db import models
from members.models import Member

class Api(models.Model):
	def __unicode__(self):
		return self.title
	title = models.CharField(max_length=25)
	icon = models.ImageField(upload_to='apis/icons/')
	brief_desc = models.CharField(max_length=50)
	full_desc = models.TextField(max_length=250)
	author = models.ForeignKey(Member)

	
