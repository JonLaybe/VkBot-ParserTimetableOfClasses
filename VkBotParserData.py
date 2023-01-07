import ParserData
from accessify import private, protected
import Timetable
from dotenv import dotenv_values
class VkBotParserData(ParserData.ParserData):
	@private
	def ParsingTimetableData(self, html_text, value):
		html_text_card_table = self.ParsingHTMLCodeOnlyTag(f'<html>{html_text[0]}</html>', 'td')
		timetable = Timetable.Timetable(value)#Timetable
		count_number = -1#number of lessons on a given day
		numbers_less_day = []#array of number of lessons per day
		days_week = []#days of the week
		nums_lesson = []
		time_lesson = []
		names_lesson = []
		teachers = []
		cabinets = []
		count = 0
		for item in html_text_card_table:
			if (self.ParsingHTMLCodeOnlyTag(f'<html>{item}</html>', 'div', 'день-недели') != None):
				if (count == 0):
					nums_lesson.append(item.text[0])
					time_lesson.append(item.text[1:])
				elif (count == 1):
					names_lesson.append(item.text)
				elif (count == 2):
					teachers.append(item.text)
				elif (count == 3):
					cabinets.append(item.text)
				if (count == 3):
					numbers_less_day[count_number] += 1
					count = -1
				count += 1
			else:
				count_number += 1
				numbers_less_day.append(0)
				days_week.append(item.text)
		timetable.Numbers_lessons_day = numbers_less_day
		timetable.Days_week = days_week
		timetable.Nums_lesson = nums_lesson
		timetable.Time_lesson = time_lesson
		timetable.Names_lesson = names_lesson
		timetable.Teachers = teachers
		timetable.Cabinets = cabinets

		return timetable.ConvertToDict()
	def GetListGroups(self, html_text):
		array_groups = []
		array_temp_groups = self.ParsingHTMLCodeOnlyTag(html_text, 'a')
		for i in range(2, len(array_temp_groups)):
			text = (f'{array_temp_groups[i].text}')
			array_groups.append(text)
		return array_groups
	def ParsingTimetable(self, html_text, value):
		return self.ParsingTimetableData(self.ParsingHTMLCodeOnlyTag(html_text, 'tbody'), value)