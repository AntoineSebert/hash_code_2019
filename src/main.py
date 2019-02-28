# -*- coding: utf-8 -*-

"""
CLASSES
"""

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
		if (_orientation == 'V' and len(_data) != 2) or (_orientation == 'H' and len(_data) != 1):
			return False
		self.orientation = _orientation
		self.data = _data

class slideshow:
	data = list() # list of slides

	def __init__(self, first_slide: slide):
		self.data.append(first_slide)

	def output(self, filename):
		import os

		if(os.path.isfile('./'+filename)):
			file = open(filename, "w")
		else:
			file = open(filename, "x")

		file.write(str(len(self.data)) + "\n")
		for slide in self.data:
			string = str()
			if slide.orientation == 'H':
				string += slide.id + "\n"
			else:
				string += str(slide.data[0].id) + " " + str(slide.data[0].id) + "\n"
			"""
			for photo in slide:
				string += photo.id
			"""
			file.write(string)
		file.close()

def parse(filename: str) -> photos_list:
	datasets_folder = "../datasets/"
	file = open(datasets_folder + filename)

	def parse_line(line: str, index: int) -> photo:
		photo_attributes = line[:-1].split(' ')

		return photo(index, photo_attributes[1], photo_attributes[2:])

	file.readline()
	_photos_list = photos_list(parse_line(file.readline(), 0))
	photos_number = 1

	for line in file:
		parse_line(line, photos_number)
		photos_number += 1

	return _photos_list

def main():
	photos = parse("a_example.txt")
	_ = slideshow(slide(photos.data[0].orientation, photos.data[0]))
	_.data.append(photos)
	_.output("test2.txt")

if __name__ == "__main__":
	main()
