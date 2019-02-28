# -*- coding: utf-8 -*-

class slide:
	data = {} # one or two photos
	orientation = {} # 'H' or 'V'
	tags = set() # set of strings
	def __init__(_orientation, _data) -> bool:
		if (_orientation == 'V' and len(_data) != 2) or (_orientation == 'H' and len(_data) != 1):
			return False
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