from django.conf.urls import patterns, url
from members.views import *

urlpatterns = patterns('',
	url(r'^(?P<member_id>\d+)/$', MemberDetailView.as_view(), name='detail'),
)	
