from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from apis.models import Api

class ApiDetailView(View):
	def get(self, request, api_id):
		api = get_object_or_404(Api, pk=api_id)
		context = {
			'api': api,
		}
		return render(request, 'api_detail.html', context)

class ApiIndexView(View):
	def get(self, request):
		apis = Api.objects.all()
		context = {
			'apis': apis,
		}
		return render(request, 'api_index.html', context)

class KitchenSinkView(View):
	def get(self, request):
		context = {}
		return render(request, 'kitchensink.html', context)
