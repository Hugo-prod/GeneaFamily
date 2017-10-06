from django.conf.urls import url
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView

from GeneaFamilyCore.models import Union
from GeneaFamilyCore.forms.union import UnionForm
from GeneaFamilyCore.views.union import CreateUnion

union_urlpatterns = [

	###########
	# Union #
	###########
	
	# Create Union and assign to Family
	url(r'^union/(?P<family_pk>\d+)/create$',
		CreateUnion.as_view(
			form_class=UnionForm,
			template_name='geneafamilycore/union/forms/create_union.html'),
				name='create_union'),

	# Update a union
	url(r'^union/(?P<family_pk>\d+)/update$',
		UpdateView.as_view(
			form_class=UnionForm,
			template_name='geneafamilycore/union/forms/update_union.html'),
				name='update_union'),

	# Delete union
	# Attention delete à partir de la family.union_fk
	url(r'^union/(?P<pk>\d+)/delete$',
		DeleteView.as_view(
			model=Union,
			template_name='geneafamilycore/union/forms/delete_member_union.html',
			success_url='/'),
				name='delete_member_union'),

	# Union's detail
	url(r'^union/(?P<pk>\d+)$',
		DetailView.as_view(
			model=Union,
			template_name='geneafamilycore/union/member_union_detail.html'),
				name='union_detail'),

	# All Unions
	url(r'^union/all$',
		ListView.as_view(
			model=Union,
			paginate_by=20,
			template_name='geneafamilycore/union/all_member_unions.html'),
				name='all_member_unions'),
]