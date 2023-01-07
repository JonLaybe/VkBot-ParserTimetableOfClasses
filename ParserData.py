from abc import ABC, abstractmethod
from accessify import private, protected
from bs4 import BeautifulSoup as bs

import GetRequests

class IParser(ABC):
	@abstractmethod
	def ParsingHTMLCode(self, html_text, tag, tag_class = None):
		pass

class ParserData(IParser):
	def __init__(self):
		pass
	def ParsingHTMLCode(self, html_text, tag, tag_class):
		soup = bs(html_text, "html.parser")
		items = soup.find_all(tag, class_= tag_class)
		return items
	def ParsingHTMLCodeOnlyTag(self, html_text, tag, class_igron = None):
		soup = bs(html_text, "html.parser")
		items = []
		if (class_igron != None and soup.find_all(tag, class_igron) != []):
			return None
		else:
			items = soup.find_all(tag)
		return items


