from django.conf.urls import url
from django.views.generic import CreateView, DeleteView

from GeneaFamilyCore.forms.child import ChildForm
from GeneaFamilyCore.models import Child
from GeneaFamilyCore.views.child import AddChild

child_urlpatterns = [

	#########
	# CHILD #
	#########
	# Add a child
	# PK: Family object (for family_fk field in Child)
	url(r'^child/(?P<family_pk>\d+)/add/child$',
		AddChild.as_view(
			form_class=ChildForm,
			template_name='geneafamilycore/child/forms/add_child.html'),
				name='add_child'),

	# Remove a child
	# PK: id Child
	url(r'^child/(?P<pk>\d+)/remove/child$',
		DeleteView.as_view(
			model=Child,
			success_url='/',
			template_name='geneafamilycore/child/forms/remove_child.html'),
				name='remove_child'),
]