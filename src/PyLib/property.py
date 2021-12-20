class Property:
	def __init__(self):
		pass
		
	def add(self, name, val):
		if type(name) != str or " " in name:
			raise SyntaxError("You put a space in the name!")
			return
		else: setattr(self, name, val)
		
	def remove(self, name):
		if type(name) != str or " " in name:
			raise SyntaxError("You put a space in the name!")
			return
		else: delattr(self, name)
		
	def get(self, name):
		if type(name) != str or " " in name:
			raise SyntaxError("You put a space in the name!")
			return
		else: getattr(self, name)
