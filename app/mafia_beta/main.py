from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
import random

red = [1, 0, 0, 1]
blue = [0, 0, 1, 1]
green = [0, 1, 0, 1]
black = [0, 0, 0, 1]
white = [1, 1, 1, 1]

DON = Image(source='iDON.jpg')
MAFIA_1 = Image(source='iMAFIA_1.jpg')
MAFIA_2 = Image(source='iMAFIA_2.jpg')
SHERIFF = Image(source='iSHERIFF.jpg')
PEACEFUL = Image(source='iPEACEFUL.jpg')

class MafiaApp(App):
	layout = BoxLayout(orientation = 'horizontal')
	numbers = []
	roles = []
	st = False
	#l = Label(text = ' ', font_size = 72, markup=True)

	def build(self):
		#layout = BoxLayout(orientation = 'horizontal')
		#Im = Image()
		button_1 = Button(background_color = blue, text = "Рассадка", font_size = 72, on_press = self.choice_of_numbers)
		button_2 = Button(background_color = green, text = "Роль", font_size = 72, on_press = self.choice_of_roles)
		clear = Button(text = 'Очистить', on_press = self.cl)
		start = Button(text = 'Start', on_press = self.start)
		self.layout.add_widget(button_1)
		self.layout.add_widget(button_2)
		#self.layout.add_widget(Im)
		#layout.add_widget(self.l)
		self.layout.add_widget(clear)
		self.layout.add_widget(start)
		return self.layout

	def choice_of_numbers(self, instance):
		if len(self.numbers) == 0:
			if self.st == True:
				instance.text = "Всё!"
			else:
				instance.text = 'Начните'
		else:
			instance.text = "Рассадка"
			number = random.choice(self.numbers)
			#self.l.color = white
			#self.l.text = '[b]' + number + '[/b]'
			self.numbers.remove(number)

	def choice_of_roles(self, instance):
		if len(self.roles) == 0:
			if self.st == True:
				instance.text = "Конец!"
			else:
				instance.text = "Начните"
		else:
			instance.text = "Роль"
			role = random.choice(self.roles)
			if role == "МИРНЫЙ":
				self.layout.add_widget(PEACEFUL, index = 2)
			if role == "ШЕРИФ":
				self.layout.add_widget(SHERIFF, index = 2)
			if role == "МАФИЯ_1":
				self.layout.add_widget(MAFIA_1, index = 2)
			if role == "МАФИЯ_2":
				self.layout.add_widget(MAFIA_2, index = 2)
			if role == "ДОН":
				self.layout.add_widget(DON, index = 2)
			#self.l.text = '[b]' + role + '[/b]'
			#if role == "МИРНЫЙ" or role == "ШЕРИФ":
				#self.l.color = red
			#if role == "МАФИЯ" or role == "ДОН":
				#self.l.color = blue
			self.roles.remove(role)

	def cl(self, instance):
		#self.l.text = ' '
		"""self.layout.remove_widget(DON)
		self.layout.remove_widget(PEACEFUL)
		self.layout.remove_widget(SHERIFF)
		self.layout.remove_widget(MAFIA_1)
		self.layout.remove_widget(MAFIA_2)"""
		self.layout.clear_widgets()

	def start(self, instance):
		self.st = True
		self.numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
		self.roles = ["МИРНЫЙ", "МИРНЫЙ", "МИРНЫЙ", "МИРНЫЙ", "МИРНЫЙ", "МИРНЫЙ", "ШЕРИФ", "МАФИЯ_1", "МАФИЯ_2", "ДОН"]


if __name__ == "__main__":
	MafiaApp().run()