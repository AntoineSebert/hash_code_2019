# -*- coding: utf-8 -*-

from classes import *

def parse(filename: str) -> List[photo]:
	file = open("C://Users//calte//OneDrive//Documents//hash_code_2019//src//"+filename)
	_photo_list = list()

	def parse_line(line: str, index: int) -> photo:
		photo_attributes = line[:-1].split(' ')

		return photo(index, photo_attributes[1], photo_attributes[2:])

	file.readline()
	_photo_list.append(parse_line(file.readline(), 0))
	photos_number = 1

	for line in file:
		_photo_list.append(parse_line(line, photos_number))
		photos_number += 1

	return _photo_list

def output(slideshow, filename):
	import os

	if(os.path.isfile('./' + filename)):
		file = open(filename, "w")
	else:
		file = open(filename, "x")

	file.write(str(len(slideshow)) + "\n")
	for slide in slideshow:
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

def convert(photos: photo_list) -> slideshow:
	return {}

def main():
	photos = parse("a_example.txt")
	for photo in photos:
		photo.print()

	slideshow = convert(photos)
	output(slideshow, "test.txt")

if __name__ == "__main__":
	main()
