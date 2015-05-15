class Piece(object):
	def __init__(self, type):
		self.type = type

	def __str__(self):
		return str(self.type)

	__repr__ = __str__
		
