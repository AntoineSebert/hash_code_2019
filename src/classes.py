# -*- coding: utf-8 -*-

from typing import List, Set

class photo:
	id = int()
	orientation = str()
	tags = set()
	used = bool()

	def __init__(self, _id: int, _orientation: str, _tags: list):
		self.id = _id;
		self.orientation = _orientation
		self.tags = _tags

	def print(self):
		print(id, orientation, tags, used)

photo_list = List[photo]

class slide:
	data = list() # one or two photos
	orientation = str()
	tags = set() # set of strings

	def __init__(self, _orientation: str, _data: list) -> bool:
		if (_orientation == 'V' and len(_data) != 2) or (_orientation == 'H' and len(_data) != 1):
			return False
		self.orientation = _orientation
		self.data = _data
		for photo in _data:
			self.tags += photo.tags

	def print(self):
		print(data, orientation, tags)

slideshow = List[slide]