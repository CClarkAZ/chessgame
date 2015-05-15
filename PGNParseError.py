class PGNParseError(Exception):
	def __init__(self, error_pos):
		self.error_pos = error_pos

	def __str__(self):
		return repr(self.error_pos)
