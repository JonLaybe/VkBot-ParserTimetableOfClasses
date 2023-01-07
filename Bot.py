from accessify import private, protected
from dotenv import dotenv_values
import time
from threading import *
import vk_api
from vk_api.utils import get_random_id
from vk_api.longpoll import VkLongPoll, VkEventType
import JsonSD
import VkBotGetRequests

class Bot:
	def __init__(self, token):
		self.__json_vk_bot = JsonSD.JsonVkBot()
		self.__vkBot_get_requests = VkBotGetRequests.VkBotGetRequests()

		self.__token = token
		self.__array_groups = {}
		self.__array_user_id = {'user_id': [{}]}
		self.__array_timetables = {}

		self.__vk_api_access = None
		self.__vk = None
		self.__long_poll = None

		self.__t1 = Thread(target = self.UpdateData)
		self.__t1.start()
	@private
	def ChackUserId(self, user_id):
		if (self.__array_user_id != None and ('user_id' in self.__array_user_id) and isinstance(self.__array_user_id['user_id'], list)):
			for item in self.__array_user_id['user_id']:
				if (str(user_id) in item):
					return True
		return False
	@private
	def ShowTimetable(self, group):
		message = ""
		timetables = self.__array_timetables[group][0]
		for item in range(0, len(timetables['day_week'])):
			message += f"-------{timetables['day_week'][item]}-------\n"
			for nums_less_day in range(0, timetables['number_lesson_day'][item]):
				message += f"{timetables['num_lesson'][nums_less_day]}({timetables['time_lesson'][nums_less_day]}) {timetables['name_lesson'][nums_less_day]}\n"

		return message
	@private
	def GetUserFirstLastName(self, user_id):
		get_user_name = self.__vk.users.get(user_ids=(user_id))[0]
		return {'id': get_user_name['id'], 'first_name': get_user_name['first_name'], 'last_name': get_user_name['last_name']}
		return message
	def LocalSerializeGroupeTask(self, user_id):
		if (self.__array_user_id['user_id'][0][str(user_id)] not in self.__array_timetables):
			self.__array_timetables[self.__array_user_id['user_id'][0][str(user_id)]] = self.__vkBot_get_requests.GetTimetable(self.__array_user_id['user_id'][0][str(user_id)])
			self.__json_vk_bot.Serialize('timetables.json', self.__array_timetables)
	@private
	def LocalSerializeGroupe(self, user_id):
		task_serialize = Thread(target = self.LocalSerializeGroupeTask, args = (user_id,))
		task_serialize.start()
	def do_auth(self):
		self.__vk_api_access = vk_api.VkApi(token=self.__token)
		self.__vk = self.__vk_api_access.get_api()
		self.__long_poll = VkLongPoll(self.__vk_api_access)
	def UpdateData(self):
		temp_array_users_id = self.__json_vk_bot.Deserialize('users.json')
		temp_array_timetables = self.__json_vk_bot.Deserialize('timetables.json')
		if (temp_array_users_id != None and ('user_id' in temp_array_users_id) and isinstance(temp_array_users_id['user_id'], list)):
			self.__array_user_id = temp_array_users_id
		if (temp_array_timetables != None):
			self.__array_timetables = temp_array_timetables
		self.__array_groups = self.__vkBot_get_requests.GetListGroups()
		#self.GetListGroups()
		#while True:
		#	time.sleep(3600)
	def SendMessage(self, user_id, message_text):
		self.__vk.messages.send(user_id=user_id, message=message_text, random_id=get_random_id())
	def run_bot(self):
		for event in self.__long_poll.listen():
			if (event.type == VkEventType.MESSAGE_NEW):
				if (event.to_me):
					request_text = event.text.lower()
					request_text_split = request_text.split()
					user = self.GetUserFirstLastName(event.user_id)
					print(f"[{user['id']}]{user['first_name']} {user['last_name']}: {event.text}")
					if (len(request_text_split) > 0 and request_text_split[0] == "!timetable"):
						if (self.ChackUserId(event.user_id) == False):
							self.__array_user_id['user_id'][0][str(event.user_id)] = None
							self.__json_vk_bot.Serialize('users.json', self.__array_user_id)
							self.SendMessage(event.user_id, f"Выберите группу")
							self.SendMessage(event.user_id, self.__array_groups)
						elif (request_text == '!timetable' and self.__array_user_id['user_id'][0][str(event.user_id)] != None):
							self.SendMessage(event.user_id, self.ShowTimetable(self.__array_user_id['user_id'][0][str(event.user_id)]))
						else:
							if (len(request_text_split) == 2):
								if (self.__array_user_id['user_id'][0][str(event.user_id)] == None):
									for item in self.__array_groups:
										if (item == request_text_split[1]):
											self.__array_user_id['user_id'][0][str(event.user_id)] = item
											self.__json_vk_bot.Serialize('users.json', self.__array_user_id)
											self.SendMessage(event.user_id, "✓")
											self.LocalSerializeGroupe(event.user_id)
							else:
								self.SendMessage(event.user_id, "Напишите: !timetable группа")