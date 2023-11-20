import kivy
from kivy.config import Config
Config.set('graphics','resizable', 0)

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
#from kivy.uix.image import Image 
#from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen

class TelaLogin(Screen):
	def LoginButton(self):
		self.manager.current = "TelaMenu"
		self.manager.transition.direction = "left"

class TelaMenu(Screen):
	def SelectTimeFilter(self):		
		self.manager.current = "ListaFiltrosHorario"
		self.manager.transition.direction = "left"

class ListaFiltrosHorario(Screen):
	def SelectTimeFilter(self):		
		self.manager.current = "ListaFiltrosHorario"
		self.manager.transition.direction = "left"

class WindowManager(ScreenManager):
	pass

Window.size = (480,800)
kv = Builder.load_file('design.kv')

#class MyLayout(TabbedPanel):	
	#def press(self):
		#string1 = self.ids.textbox1.text
		#self.ids.label1.text = f'cccccc: {string1}'
		#print(f'Hello {string1}, your password is {password}')
		#self.add_widget(Label(text=f"Hello {name}, your password is {password

class TheApp(App):
	def build(self):
		# Window.clearcolor = (1,1,1,1) #Mudar cor do Background
		return kv

if __name__ == '__main__':
	TheApp().run()
