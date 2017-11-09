from django.forms import ModelForm

from GeneaFamilyCore.models import Source, SourceMember


class SourceForm(ModelForm):
	""" Create source. """

	class Meta:
		model = Source
		fields =[	'source_type',
					'title',
					'img_upload',
					'url_link',
					'page_link',
					'additional_note',]


class SourceInvolvedMemberForm(ModelForm):
	""" Add involved member to source. """

	class Meta:
		model = SourceMember
		fields =[	'member_fk']