from kivymd.app import MDApp
from kivy.lang import Builder

KV = '''
MDScreen:
    Image: 
        source: 'gif_app1.gif'

'''

class MyApp(MDApp):
    def build(self):
        return Builder.load_string(KV)
    

MyApp().run()