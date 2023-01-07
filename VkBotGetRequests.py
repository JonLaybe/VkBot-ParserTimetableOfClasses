import GetRequests
import ParserData
import Timetable
import VkBotParserData
from dotenv import dotenv_values

class VkBotGetRequests(GetRequests.GetRequests):
	def __init__(self):
		self.__timetables = []
		self.__parser = ParserData.ParserData()
		self.__vk_bot_parser = VkBotParserData.VkBotParserData()
	def JsonTimetable(self):
		pass
	def GetTimetable(self, value):
		url = dotenv_values("val.env")['url1_group'] + value + dotenv_values("val.env")['url2_group']
		if (self.GetRequest(url)):
			html_text = self.GetHTMLCodeEncoding('iso-8859-1', 'utf-8')
			return self.__vk_bot_parser.ParsingTimetable(html_text, value)
	def GetListGroups(self):
		if (self.GetRequest(dotenv_values("val.env")['url_groups'])):
			return self.__vk_bot_parser.GetListGroups(self.GetHTMLCodeEncoding('iso-8859-1', 'utf-8'))