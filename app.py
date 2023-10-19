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

Window.size = (480,800)
Builder.load_file('Login.kv')

class MyLayout(Widget):	
	def press(self):
		string1 = self.ids.textbox1.text
		#self.ids.label1.text = f'cccccc: {string1}'
		#print(f'Hello {string1}, your password is {password}')
		#self.add_widget(Label(text=f"Hello {name}, your password is {password

class TheApp(App):
	def build(self):
		# Window.clearcolor = (1,1,1,1) #Mudar cor do Background
		return MyLayout()

if __name__ == '__main__':
	TheApp().run()
