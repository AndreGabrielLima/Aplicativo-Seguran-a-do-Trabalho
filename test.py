from kivy.uix.image import AsyncImage
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout

Builder.load_string('''
<GifViewer>:
    AsyncImage:
        source: 'load.gif'
''')

class GifViewer(MDBoxLayout):
    pass

class MyApp(MDApp):
    def build(self):
        return GifViewer()

MyApp().run()