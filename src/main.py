# -*- coding: utf-8 -*-

from enum import Enum

class orientation(Enum):
	H = 'H'
	V = 'V'

class photo:
	id = 0
	orientation = {}
	tags = []
	used = False

	def __init__(self, _id: int, orien: orientation, tag: str):
		self.id = _id;
		self.orientation = orien
		self.tags = tag

class photos_list:
	data = list()
	def __init__(self, first_photo: photo):
		self.data.append(first_photo)

class slide:
	data = {} # one or two photos
	orientation = {}
	tags = set() # set of strings
	def __init__(self, _orientation: orientation, _data) -> bool:
		if (_orientation == V and len(_data) != 2) or (_orientation == H and len(_data) != 1):
			return False
		self.orientation = _orientation
		self.data = _data

class slideshow:
	data = list() # list of slides
	def __init__(self, first_slide: slide):
		self.data.append(first_slide)

def parse(filename: str) -> photos_list:
	datasets_folder = "../datasets/"
	file = open(datasets_folder + filename)

	def parse_line(line: str) -> photo:
		print(line[:-1].split(' '))
		return {}

	file.readline()
	_photos_list = photos_list(parse_line(file.readline()))

	for line in file:
		parse_line(line)

	return _photos_list

def output(file):
	if(os.path.isfile('./'+filename)):
		file = open(filename, "w")
	else:
		file = open(filename, "x")

	file.write(len(data))
	for line in data:
		file.write(line)
	file.close()

def main():
	"""Script entry point"""
	photos = parse("a_example.txt")

if __name__ == "__main__":
	main()
