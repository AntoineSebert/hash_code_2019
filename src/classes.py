# -*- coding: utf-8 -*-

from typing import List, Set

""" PHOTO =========================================================================================================="""
class photo:
	id = int()
	orientation = str()
	tags = set()
	used = bool()

	def __init__(self, _id: int, _orientation: str, _tags: list):
		self.id = _id;
		self.orientation = _orientation
		self.tags = _tags

""" PHOTO LIST ====================================================================================================="""
photo_list = List[photo]

""" SLIDE =========================================================================================================="""
class slide:
	data = list() # one or two photos
	orientation = str()
	tags = set() # set of strings

	def __init__(self, _orientation: str, _data: list) -> bool:
		if (_orientation == 'V' and len(_data) != 2) or (_orientation == 'H' and len(_data) != 1):
			return False
		self.orientation = _orientation
		self.data = _data

""" SLIDESHOW ======================================================================================================"""
slideshow = List[slide]