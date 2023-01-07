from abc import ABC, abstractmethod
from accessify import private, protected
import requests

class IGetRequestSite(ABC):
	@abstractmethod
	def GetRequest(self, url):
		pass
	@abstractmethod
	def GetHTMLCode(self):
		pass
	@abstractmethod
	def GetHTMLCodeEncoding(self, encode, decode):
		pass

class ErrorParser():
	def ErrorTextNoSiteRequest(self):
		return "ErrorRequest: No site request!"

class GetRequests(IGetRequestSite):
	def __init__(self):
		self.__errors_except = ErrorParser()

		self.__can_request = False
		self.__url = None
		self.__request = None
		self.__html_text = ""
	@property
	def can_request(self):
		return self.__can_request
	def GetRequest(self, url):
		self.__url = url;
		self.__request = requests.get(url)
		if(self.__request.status_code == 200):
			self.__can_request = True
			return True
		self.__can_request = False
		return False
	def GetHTMLCode(self):
		if (self.__can_request):
			self.__html_text = self.__request.text
			return self.__html_text
		else:
			return self.__errors_except.ErrorTextNoSiteRequest()
	#iso-8859-1
	def GetHTMLCodeEncoding(self, encode, decode):
		if (self.__can_request):
			self.__html_text = self.__request.text
			self.__html_text = self.__html_text.encode(encode).decode(decode)
			return self.__html_text
		else:
			return self.__errors_except.ErrorTextNoSiteRequest()