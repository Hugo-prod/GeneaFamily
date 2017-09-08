from django.conf.urls import url
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView

from GeneaFamilyCore.models import Member
from GeneaFamilyCore.forms.member import MemberForm

member_urlpatterns = [

	##########
	# MEMBER #
	##########
	# Create a member
	url(r'^member/create$',
		CreateView.as_view(
			form_class=MemberForm,
			template_name='geneafamilycore/member/forms/create_member.html'),
				name='create_member'),

	# Update a member
	url(r'^member/(?P<pk>\d+)/update$',
		UpdateView.as_view(
			model=Member,
			form_class=MemberForm,
			template_name='geneafamilycore/member/forms/update_member.html'),
				name='update_member'),

	# Delete member
	url(r'^member/(?P<pk>\d+)/delete$',
		DeleteView.as_view(
			model=Member,
			template_name='geneafamilycore/member/forms/delete_member.html',
			success_url='/'),
				name='delete_member'),

	# Member's detail
	url(r'^member/(?P<pk>\d+)$',
		DetailView.as_view(
			model=Member,
			template_name='geneafamilycore/member/member_detail.html'),
				name='member_detail'),

	# All Members
	url(r'^member/all$',
		ListView.as_view(
			model=Member,
			paginate_by=20,
			template_name='geneafamilycore/member/all_members.html'),
				name='all_members'),
]