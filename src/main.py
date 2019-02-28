# -*- coding: utf-8 -*-

from enum import Enum

class orientation(Enum):
	H = 'H'
	V = 'V'

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

def parse(filename: str) -> slideshow:
	datasets_folder = "../datasets/"
	file = open(datasets_folder + filename)
	file.readline()
	for line in file:
		print(line[:-1])


def main():
	"""Script entry point"""
	parse("a_example.txt")

if __name__ == "__main__":
	main()