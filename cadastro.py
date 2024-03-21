from kivymd.app import MDApp
from kivy.lang import Builder

KV = '''
MDScrollView:
    MDBoxLayout:
        md_bg_color: 'blue'
        orientation:'vertical'
            
        MDBoxLayout:
            orientation: 'vertical'
            size_hint_y:.75
            cols:2
            padding:[dp(15),dp(15),dp(15),dp(35)]
            spacing:dp(15)
            MDCard:
                padding:dp(10)
                spacing:dp(10)
                radius:dp(25)
                ripple_behavior: True
                MDFloatLayout:
                    Image:
                        source: 'foto1_insa.png'
                        pos_hint: {'center_x': .13, 'center_y': .4}
                MDFloatLayout:    
                    MDLabel:
                        adaptive_size: True
                        text: 'Barulho Excessivo'
                        
                        pos_hint: {'center_x': .01, 'center_y': .6}                       
                
            MDCard:
                padding:dp(10)
                spacing:dp(10)
                radius:dp(25)
                ripple_behavior: True
                MDFloatLayout:
                    Image:
                        source: 'foto2_insa.png'
                        pos_hint: {'center_x': .13, 'center_y': .6}
                MDFloatLayout:    
                    MDLabel:
                        adaptive_size: True
                        text: 'Temperatura'
                        
                        pos_hint: {'center_x': .01, 'center_y': .6}
            MDCard:
               
                padding:dp(10)
                spacing:dp(10)
                radius:dp(25)
                ripple_behavior: True
                MDFloatLayout:
                    Image:
                        source: 'foto3_insa.png'
                        pos_hint: {'center_x': .13, 'center_y': .6}
                MDFloatLayout:    
                    MDLabel:
                        adaptive_size: True
                        text: 'Iluminação'
                        
                        pos_hint: {'center_x': .01, 'center_y': .6}
            MDCard:
               
                padding:dp(10)
                spacing:dp(10)
                radius:dp(25)
                ripple_behavior: True
                MDFloatLayout:
                    Image:
                        source: 'foto4_insa.png'
                        pos_hint: {'center_x': .13, 'center_y': .5}
                MDFloatLayout:    
                    MDLabel:
                        adaptive_size: True
                        text: 'Computadores e Periféricos'
                        
                        pos_hint: {'center_x': .01, 'center_y': .6}

            MDCard:
               
                padding:dp(10)
                spacing:dp(10)
                radius:dp(25)
                ripple_behavior: True
                MDFloatLayout:
                    Image:
                        source: 'foto5_insa.png'
                        pos_hint: {'center_x': .13, 'center_y': .5}
                MDFloatLayout:    
                    MDLabel:
                        adaptive_size: True
                        text: 'Mobiliário'
                        
                        pos_hint: {'center_x': .01, 'center_y': .6}
            MDCard:
               
                padding:dp(10)
                spacing:dp(10)
                radius:dp(25)
                ripple_behavior: True
                MDFloatLayout:
                    Image:
                        source: 'foto6_insa.png'
                        pos_hint: {'center_x': .13, 'center_y': .5}
                MDFloatLayout:    
                    MDLabel:
                        adaptive_size: True
                        text: 'Saúde'
                        
                        pos_hint: {'center_x': .01, 'center_y': .6}
            
            MDCard:
               
                padding:dp(10)
                spacing:dp(10)
                radius:dp(25)
                ripple_behavior: True
                MDFloatLayout:
                    Image:
                        source: 'foto7_insa.png'
                        pos_hint: {'center_x': .13, 'center_y': .5}
                MDFloatLayout:    
                    MDLabel:
                        adaptive_height: True
                        mode: 'fill'
                        text: 'Acessibilidade'
                        
                        pos_hint: {'center_x': .18, 'center_y': .6}

            MDCard:
               
                padding:dp(10)
                spacing:dp(10)
                radius:dp(25)
                ripple_behavior: True
                MDFloatLayout:
                    Image:
                        source: 'foto8_insa.png'
                        pos_hint: {'center_x': .13, 'center_y': .5}
                MDFloatLayout:    
                    MDLabel:
                        adaptive_height: True
                        mode: 'fill'
                        text: 'Outros'
                        
                        pos_hint: {'center_x': .18, 'center_y': .6}
'''

class MyApp(MDApp):
    def build(self):
        return Builder.load_string(KV)
    
MyApp().run()