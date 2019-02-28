# -*- coding: utf-8 -*-

from typing import List, Set

tag_set = Set[str]

class photo:
	id = int()
	orientation = str()
	tags = set()
	used = bool()

	def __init__(self, _id: int, _orientation: str, _tags: Set[str]):
		self.id = _id;
		self.orientation = _orientation
		self.tags = _tags

	def print(self):
		print(self, self.id, self.orientation, self.tags, self.used)

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
		print(self, self.data, self.orientation, self.tags)

	def to_string(self) -> str:
		if len(data) == 1:
			return data[0].id
		return data[0].id + data[1].id

slideshow = List[slide]