from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.clock import Clock

from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition, FadeTransition, NoTransition
from kivy.uix.floatlayout import FloatLayout


Builder.load_string("""

<FirstScreen>:
    orientation: "vertical"
    Image:
        id: gif
        source: 'load.gif'
        pos: self.pos
        size_hint: None, None
        size: root.size
        allow_stretch: True
        keep_ratio: False
        anim_delay: -1
        anim_loop: 1
        
<SecondScreen>:
    orientation: "vertical"
    Label:
        text:"Second Screen"
        
""")


class FirstScreen(Screen, FloatLayout):
    secs = 0

    def __init__(self, **kwargs):
        super(FirstScreen, self).__init__(**kwargs)
        self.orientation = "vertical"
        Clock.schedule_interval(self.update_time, 1)

    def update_time(self, sec):
        self.secs = self.secs+1
        '''  30 seconds'''
        if self.secs == 30:
            self.manager.current = 'second'

    def on_enter(self):
        self.ids.gif.anim_delay = 0.10



class SecondScreen(Screen, FloatLayout):

    def __init__(self, **kwargs):
        super(SecondScreen, self).__init__(**kwargs)
        self.orientation = "vertical"


class ExampleApp(App):

    def build(self):
        sm = ScreenManager(transition=NoTransition())
        sm.add_widget(FirstScreen(name='first'))
        sm.add_widget(SecondScreen(name='second'))
        return sm


if __name__ == "__main__":
    ExampleApp().run()