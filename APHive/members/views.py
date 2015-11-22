from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from members.models import Member
from apis.models import Api

class MemberDetailView(View):
	def get(self, request, member_id):
		m = get_object_or_404(Member, pk=member_id)
		apis = Api.objects.filter(author_id=member_id)
		context = {
			'member': m,
			'apis' : apis,
		}
		return render(request, 'member_detail.html', context)

