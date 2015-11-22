from django.test import TestCase
from django.utils import timezone
from members.models import Member

def create_member(fname,lname,email):
	t = timezone.now()
	return Member(first_name=fname,last_name=lname,joined=t,email=email)


class MemberModelTests(TestCase):
	def test_full_name_built_correctly(self):
		member = create_member('nolan','ramsden','nolan_ramsden@outlook.com')
		self.assertEqual('nolan ramsden', member.full_name)
