from django.conf import settings
from django.conf.urls import patterns, url
from django.conf.urls.static import static
from apis.views import *

urlpatterns = patterns('',
	url(r'^$', ApiIndexView.as_view(), name='home'),
	url(r'^kitchensink/$', KitchenSinkView.as_view(), name='kitchensink'),
	url(r'^(?P<api_id>\d+)/$', ApiDetailView.as_view(), name='detail'),	
)
