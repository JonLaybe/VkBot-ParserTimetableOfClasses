class Timetable:
	"""docstring for Timetable
	{09.07.10:[{'numbers_lessons_day': []}, {день недели:[]}, {номер пары:[]}, {часы пар:[]}, {название пар:[]}, {преподователь:[]}, {аудитория:[]}]}
	"""
	def __init__(self, name_group):
		self.name_group = name_group
		self.numbers_lessons_day = None
		self.days_week = None
		self.nums_lesson = None
		self.time_lesson = None
		self.names_lesson = None
		self.teachers = None
		self.cabinets = None
	@property
	def Name_group(self):
		return self.name_group
	@property
	def Numbers_lessons_day(self):
		return self.numbers_lessons_day
	@property
	def Days_week(self):
		return self.days_week
	@property
	def Nums_lesson(self):
		return self.nums_lesson
	@property
	def Time_lesson(self):
		return self.time_lesson
	@property
	def Names_lesson(self):
		return self.names_lesson
	@property
	def Teachers(self):
		return self.teachers
	@property
	def Cabinets(self):
		return self.cabinets
	@Numbers_lessons_day.setter
	def Numbers_lessons_day(self, number_lessons_day):
		self.numbers_lessons_day = number_lessons_day
	@Days_week.setter
	def Days_week(self, day_week):
		self.days_week = day_week
	@Nums_lesson.setter
	def Nums_lesson(self, num_lesson):
		self.nums_lesson = num_lesson
	@Time_lesson.setter
	def Time_lesson(self, time_lesson):
		self.time_lesson = time_lesson
	@Names_lesson.setter
	def Names_lesson(self, name_lesson):
		self.names_lesson = name_lesson
	@Teachers.setter
	def Teachers(self, teacher):
		self.teachers = teacher
	@Cabinets.setter
	def Cabinets(self, cabinet):
		self.cabinets = cabinet
	def ConvertToDict(self):
		return [{'day_week': self.Days_week, 'number_lesson_day': self.Numbers_lessons_day, 'num_lesson': self.Nums_lesson, 'time_lesson': self.Time_lesson, 'name_lesson': self.Names_lesson, 'teacher': self.Teachers, 'cabinet': self.Cabinets}]
	def ConvertToTimetable(self, timetable_dict):
		self.Numbers_lessons_day = numbers_less_day
		self.Days_week = days_week
		self.Nums_lesson = nums_lesson
		self.Time_lesson = time_lesson
		self.Names_lesson = names_lesson
		self.Teachers = teachers
		self.Cabinets = cabinets