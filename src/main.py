# -*- coding: utf-8 -*-

class slide:
	data = {}
	orientation = {}
	tags = list()
	def __init__(_orientation, _data) -> bool:
		"""
		if (self.orientation == 'V' and len(self.data) != 2)
		or (self.orientation == 'H' and len(self.data) != 1):
			return False
		"""
		self.orientation = _orientation
		self.data = _data

class slideshow:
	data = list() # list of slides
	def __init__(first_slide: slide):
		data.append(photo)

def main():
	"""Script entry point"""

if __name__ == "__main__":
	main()