from django.forms import ModelForm

from GeneaFamilyCore.models import Source


class SourceForm(ModelForm):
	""" Create source. """

	class Meta:
		model = Source
		fields =[	'source_type',
					'img_upload',
					'url_link',
					'page_link',
					'additional_note',]

