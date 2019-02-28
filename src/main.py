# -*- coding: utf-8 -*-

from classes import *

def parse(filename: str) -> List[photo]:
	datasets_folder = "../datasets/"
	file = open(datasets_folder + filename)
	_photo_list = list()

	def parse_line(line: str, index: int) -> photo:
		photo_attributes = line[:-1].split(' ')

		return photo(index, photo_attributes[0], photo_attributes[2:])

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
		file.write(slide.to_string())
	file.close()

def convert(photos: photo_list) -> slideshow:
	_slideshow = list()
	dummy_tags = set()
	dummy_tags.add("test")
	dummy_photo = photo(0, 'H', dummy_tags)
	dummy_list = list()
	dummy_list.append(dummy_photo)
	_slideshow.append(slide('H', dummy_list))
	return _slideshow

def main():
	photos = parse("a_example.txt")
	for photo in photos:
		photo.print()

	slideshow = convert(photos)
	for slide in slideshow:
		slide.print()

	output(slideshow, "test.txt")

if __name__ == "__main__":
	main()
