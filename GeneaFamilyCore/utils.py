def clean_n_format(data):
	""" Cleanning and formatting process.
		- Removing useless whitespaces
		- Convert all words in 'Title Case'
	"""
	return " ".join(data.split()).title()