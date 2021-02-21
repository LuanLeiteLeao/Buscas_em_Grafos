class State:
	def __init__(self, name):
		self.name = name
		self.adjacencies = []

	def __str__(self):
		return self.name

