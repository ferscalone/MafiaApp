from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import random

red = [1, 0, 0, 1]
blue = [0, 0, 1, 1]
green = [0, 1, 0, 1]
black = [0, 0, 0, 1]
white = [1, 1, 1, 1]

class MafiaApp(App):
	layout = BoxLayout(orientation = 'vertical')
	numbers = []
	roles = []
	numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
	roles = ["МИРНЫЙ", "МИРНЫЙ", "МИРНЫЙ", "МИРНЫЙ", "МИРНЫЙ", "МИРНЫЙ", "ШЕРИФ", "МАФИЯ", "МАФИЯ", "ДОН"]
	#st = False
	l = Label(text = ' ', font_size = 72, markup=True)

	def build(self):
		button_1 = Button(background_color = blue, text = "Рассадка", font_size = 72, on_press = self.choice_of_numbers)
		button_2 = Button(background_color = green, text = "Роль", font_size = 72, on_press = self.choice_of_roles)
		clear = Button(text = 'Очистить', on_press = self.cl)
		start = Button(text = 'Start', on_press = self.start)
		self.layout.add_widget(button_1)
		self.layout.add_widget(button_2)
		self.layout.add_widget(self.l)
		self.layout.add_widget(clear)
		self.layout.add_widget(start)
		return self.layout

	def choice_of_numbers(self, instance):
		if len(self.numbers) == 0:
			instance.text = "Всё"
		else:
			instance.text = "Рассадка"
			number = random.choice(self.numbers)
			self.l.color = white
			self.l.text = '[b]' + number + '[/b]'
			self.numbers.remove(number)

	def choice_of_roles(self, instance):
		if len(self.roles) == 0:
			instance.text = "Конец"
		else:
			instance.text = "Роль"
			role = random.choice(self.roles)
			self.l.text = '[b]' + role + '[/b]'
			if role == "МИРНЫЙ" or role == "ШЕРИФ":
				self.l.color = red
			if role == "МАФИЯ" or role == "ДОН":
				self.l.color = blue
			self.roles.remove(role)

	def cl(self, instance):
		self.l.text = ' '

	def start(self, instance):
		#self.st = True
		self.numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
		self.roles = ["МИРНЫЙ", "МИРНЫЙ", "МИРНЫЙ", "МИРНЫЙ", "МИРНЫЙ", "МИРНЫЙ", "ШЕРИФ", "МАФИЯ", "МАФИЯ", "ДОН"]


if __name__ == "__main__":
	MafiaApp().run()
