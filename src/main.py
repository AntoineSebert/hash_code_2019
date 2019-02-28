# -*- coding: utf-8 -*-

from classes import *

""" PARSE =========================================================================================================="""
def parse(filename: str) -> list:
	datasets_folder = "../datasets/"
	file = open(datasets_folder + filename)

	def parse_line(line: str, index: int) -> photo:
		photo_attributes = line[:-1].split(' ')

		return photo(index, photo_attributes[1], photo_attributes[2:])

	file.readline()
	_photo_list = photo_list(parse_line(file.readline(), 0))
	photos_number = 1

	for line in file:
		parse_line(line, photos_number)
		photos_number += 1

	return _photo_list

""" OUTPUT ========================================================================================================="""
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


""" CONVERT ========================================================================================================"""
def convert(photos: photo_list) -> slideshow:
	return {}


""" ENTRY POINT ===================================================================================================="""
def main():
	photos = parse("a_example.txt")
	slideshow = convert(photos)
	output(slideshow, "test.txt")

if __name__ == "__main__":
	main()
