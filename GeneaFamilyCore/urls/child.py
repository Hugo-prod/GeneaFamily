from django.conf.urls import url
from django.views.generic import CreateView, DeleteView

from GeneaFamilyCore.models import Child
from GeneaFamilyCore.forms.child import ChildForm
from GeneaFamilyCore.views.child import AddChild, DeleteChild

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
		DeleteChild.as_view(
			model=Child,
			template_name='geneafamilycore/child/forms/remove_child.html'),
				name='remove_child'),
]