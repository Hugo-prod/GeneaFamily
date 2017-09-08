from django.conf.urls import url
from django.views.generic import TemplateView, CreateView, UpdateView, DetailView, DeleteView, ListView

from .views import *
from .models import Member
from .forms import *

urlpatterns = [
	url(r'^$', 
		TemplateView.as_view(template_name='generic/index.html'), name='home'),

##########
# MEMBER #
##########

	# Create a member
	url(r'^member/create$',
		CreateView.as_view(
			form_class=MemberForm,
			template_name='geneafamilycore/forms/create_member.html'),
				name='create_member'),

	# Update a member
	url(r'^member/(?P<pk>\d+)/update$',
		UpdateView.as_view(
			model=Member,
			form_class=MemberForm,
			template_name='geneafamilycore/forms/update_member.html'),
				name='update_member'),

	# Delete member
	url(r'^member/(?P<pk>\d+)/delete$',
		DeleteView.as_view(
			model=Member,
			template_name='geneafamilycore/forms/delete_member.html',
			success_url='/'),
				name='delete_member'),

	# Member's detail
	url(r'^member/(?P<pk>\d+)$',
		DetailView.as_view(
			model=Member,
			template_name='geneafamilycore/member_detail.html'),
				name='member_detail'),

	# All Members
	url(r'^member/all$',
		ListView.as_view(
			model=Member,
			paginate_by=20,
			template_name='geneafamilycore/all_members.html'),
				name='all_members'),

]