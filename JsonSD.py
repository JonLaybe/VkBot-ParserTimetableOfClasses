import json
from accessify import private, protected
from threading import *

class JsonSD():
	def Serialize(self, path, data):
		str_json = json.dumps(data)
		with open(path, 'w') as file:
			file.write(str_json)
			file.close()
	def Deserialize(self, path):
		try:
			with open(path) as file:
				str_json = json.load(file)
				file.close()
				return str_json
		except FileNotFoundError:
			return None
class JsonVkBot():
	def __init__(self):
		self.__json = JsonSD()
	def Serialize(self, path, data):
		task_serialize = Thread(target = self.__json.Serialize, args = (path ,data,))
		task_serialize.start()
	def Deserialize(self, path):
		return self.__json.Deserialize(path)
	def CheckIdUser(self, user_vk_id):
		json_sd = self.Deserialize()
		if (json_sd != None and ('user_id' in json_sd) and isinstance(json_sd['user_id'], list)):
			for item in json_sd['user_id'][0]:
				if (str(user_vk_id) in item):
					return True
		return False