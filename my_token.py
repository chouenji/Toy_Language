class Token:
	def __init__(self,tag="", val=""):
		self.val = val
		self.type = tag

	def __repr__(self):
		return f"({self.val}, {self.type})"