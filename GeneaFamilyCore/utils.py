def clean_n_format(data, format_type):
	""" Cleanning and formatting process.
		- Removing useless whitespaces
		- Convert all words in 'Title Case'
	"""

	if format_type == 'T': # = Title Case
		return " ".join(data.split()).title()

	if format_type == 'C': # = Capitalize str
		return " ".join(data.lower().split()).capitalize()
