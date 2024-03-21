from kivymd.uix.card import MDCard
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window


Window.size = (350,600)

Builder.load_string('''


<JanelaPrincipal>:
    name: 'janela_principal'
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            shadow_color: 'blue'
            title: 'Ergo'
            elevation: 2
            anchor_title: 'left'
            right_action_items: [['theme-light-dark', lambda x: app.change_color()]]
                
        MDFloatLayout:
            Image:  
                source: 'newphoto.png'
                pos_hint: {'center_x': .5, 'center_y': .8}
                size_hint: .4, .4
            MDTextField:
                icon_right: 'email'
                size_hint_x: .9
                hint_text: 'Email'
                pos_hint: {'center_x': .5, 'center_y': .6}
            MDTextField:
                icon_right: 'lock'
                password: True
                size_hint_x: .9
                hint_text: 'Senha'
                pos_hint: {'center_x': .5, 'center_y': .5}
            MDRaisedButton:
                size_hint_x: .9
                pos_hint: {'center_x': .5, 'center_y': .4}
                text: 'Login'
                on_release:
                    app.root.current = 'janela1'
            MDRaisedButton:
                size_hint_x: .9
                pos_hint: {'center_x': .5, 'center_y': .3}
                text: 'Cadastro'
                on_release:
                    app.root.current = 'cadastro'
            MDTextButton:
                pos_hint: {'center_x': .5, 'center_y': .2}
                text: 'Esqueceu sua senha?'
<Cadastro>:
    name: 'cadastro'
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            elevation: 2
            left_action_items: [['arrow-left', lambda x: app.voltar_login()]]
        MDFloatLayout:
            Image:  
                source: 'newphoto.png'
                pos_hint: {'center_x': .5, 'center_y': .8}
                size_hint: .3, .3
            MDTextField:
                icon_right: 'email'
                size_hint_x: .9
                hint_text: 'Cadastrar Email'
                pos_hint: {'center_x': .5, 'center_y': .6}
            MDTextField:
                icon_right: 'lock'
                password: True
                size_hint_x: .9
                hint_text: 'Cadastrar Senha'
                pos_hint: {'center_x': .5, 'center_y': .5}
            MDTextField:
                icon_right: 'lock'
                password: True
                size_hint_x: .9
                hint_text: 'Confirmar Senha'
                pos_hint: {'center_x': .5, 'center_y': .4}
            MDRaisedButton:
                size_hint_x: .9
                pos_hint: {'center_x': .5, 'center_y': .3}
                text: 'Cadastrar'

<Janela1>:
    name: 'janela1'
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
                on_release: app.guia_postural_press()
                padding:dp(10)
                spacing:dp(10)
                radius:dp(25)
                ripple_behavior: True
                MDFloatLayout:
                    Image:
                        source: 'fotomenu.png'
                        pos_hint: {'center_x': .13, 'center_y': .4}
                MDFloatLayout:    
                    MDLabel:
                        adaptive_size: True
                        text: 'GUIA POSTURAL'
                        
                        pos_hint: {'center_x': .01, 'center_y': .6}                       
                
            MDCard:
                on_release: app.ex_laboral()
                padding:dp(10)
                spacing:dp(10)
                radius:dp(25)
                ripple_behavior: True
                MDFloatLayout:
                    Image:
                        source: 'segundaFoto.png'
                        pos_hint: {'center_x': .13, 'center_y': .6}
                MDFloatLayout:    
                    MDLabel:
                        adaptive_size: True
                        text: 'EXERCÍCIO LABORAL'
                        
                        pos_hint: {'center_x': .01, 'center_y': .6}
            MDCard:
                on_release: app.insa()
                padding:dp(10)
                spacing:dp(10)
                radius:dp(25)
                ripple_behavior: True
                MDFloatLayout:
                    Image:
                        source: 'terceiraFoto.png'
                        pos_hint: {'center_x': .13, 'center_y': .6}
                MDFloatLayout:    
                    MDLabel:
                        adaptive_size: True
                        text: 'INSATISFAÇÕES'
                        
                        pos_hint: {'center_x': .01, 'center_y': .6}
            MDCard:
                on_release: app.faleConosco()
                padding:dp(10)
                spacing:dp(10)
                radius:dp(25)
                ripple_behavior: True
                MDFloatLayout:
                    Image:
                        source: 'quartaFoto.png'
                        pos_hint: {'center_x': .13, 'center_y': .5}
                MDFloatLayout:    
                    MDLabel:
                        adaptive_size: True
                        text: 'FALE CONOSCO'
                        
                        pos_hint: {'center_x': .01, 'center_y': .6}

            MDCard:
               
                padding:dp(10)
                spacing:dp(10)
                radius:dp(25)
                ripple_behavior: True
                MDFloatLayout:
                    Image:
                        source: 'quintaFoto.png'
                        pos_hint: {'center_x': .13, 'center_y': .5}
                MDFloatLayout:    
                    MDLabel:
                        adaptive_size: True
                        text: 'ANÁLISE DE POSTURA'
                        
                        pos_hint: {'center_x': .01, 'center_y': .6}
            MDCard:
                on_release: app.quest()
                padding:dp(10)
                spacing:dp(10)
                radius:dp(25)
                ripple_behavior: True
                MDFloatLayout:
                    Image:
                        source: 'sextaFoto.png'
                        pos_hint: {'center_x': .13, 'center_y': .5}
                MDFloatLayout:    
                    MDLabel:
                        adaptive_size: True
                        text: 'QUESTIONÁRIO'
                        
                        pos_hint: {'center_x': .01, 'center_y': .6}
            
            MDCard:
               
                padding:dp(10)
                spacing:dp(10)
                radius:dp(25)
                ripple_behavior: True
                MDFloatLayout:
                    Image:
                        source: 'sextaFoto.png'
                        pos_hint: {'center_x': .13, 'center_y': .5}
                MDFloatLayout:    
                    MDLabel:
                        adaptive_height: True
                        mode: 'fill'
                        text: 'FERRAMENTAS DE ACESSIBILIDADE'
                        
                        pos_hint: {'center_x': .18, 'center_y': .6}
                    

<GuiaPostural>:
    name: 'guia_postural'
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: 'blue'
        MDTopAppBar:
            title: 'Guia Postural'
            elevation: 2
            anchor_title: 'center'
            left_action_items: [['arrow-left', lambda x: app.voltar()]]
            
        MDBoxLayout:
            orientation: 'vertical'
            size_hint_y:.75
            cols:2
            padding:[dp(15),dp(15),dp(15),dp(35)]
            spacing:dp(15)
            MDCard:
                on_release: app.guia1()
                padding:dp(10)
                spacing:dp(10)
                radius:dp(25)
                ripple_behavior: True
                
                Image:
                    source: 'guia_post1.jpg'
                    size_hint_y: 1
                    pos_hint: {'center_x': .13, 'center_y': .4}
            
            MDCard:
                on_release: app.guia2()
                padding:dp(10)
                spacing:dp(10)
                radius:dp(25)
                ripple_behavior: True
                
                Image:
                    source: 'guia_post2.jpg'
                    pos_hint: {'center_x': .13, 'center_y': .4}
        
            MDCard:
                on_release: app.guia3()
                padding:dp(10)
                spacing:dp(10)
                radius:dp(25)
                ripple_behavior: True
                
                Image:
                    source: 'guia_post3.jpg'
                    pos_hint: {'center_x': .13, 'center_y': .5}

            MDCard:
                on_release: app.guia4()
                padding:dp(10)
                spacing:dp(10)
                radius:dp(25)
                ripple_behavior: True
              
                Image:
                    source: 'guia_post4.jpg'
                    pos_hint: {'center_x': .13, 'center_y': .4}


<PrimeiraImagem>:
    name: 'primeira_imagem'

    MDBoxLayout:
        orientation: 'vertical'
        
        MDTopAppBar:
            elevation: 2
            left_action_items: [['arrow-left', lambda x: app.guia_postural_press()]]

        MDBoxLayout:
            orientation: 'vertical'
            MDLabel:
                text: '1- A borda superior do monitor deve estar na linha reta dos olhos, mantendo a cervical reta; '
                haling: 'left'
            MDLabel:
                text: '2- As articulações dos cotovelos, quadril, joelho e pés devem estar relaxadas, a uma angulação de 90°, para facilitar a circulação do sangue pelo corpo; '
                haling: 'left'
            MDLabel:
                text: '3- Antebraços precisam ficar sempre apoiados na mesa, evitando apoiar apenas os punhos; '
            MDLabel:
                text: '4- A coluna deve ficar reta, evitando curvaturas para frente ou para trás; '
            MDLabel:
                text: '5- O ideal é que as plantas dos pés fiquem apoiadas no chão. Se houver necessidade, algum objeto que pode ser utilizado como apoio; '
            MDLabel:
                text: '6- Se possível, a altura da cadeira deve ser ajustada de modo que não pressione a parte posterior da coxa e não comprimia a região; '
            MDLabel:
                text: '7- O ideal é não ficar sentado por um tempo prolongado, levantando-se da cadeira e realizando pequenos intervalos, alterando a postura. '

<SegundaImagem>:
    name: 'segunda_imagem'

    MDBoxLayout:
        orientation: 'vertical'
        
        MDTopAppBar:
            elevation: 2
            left_action_items: [['arrow-left', lambda x: app.guia_postural_press()]]

        MDBoxLayout:
            orientation: 'vertical'
            
            MDLabel:
                text: '1. Pegue a carga o mais próximo do corpo.'
            MDLabel:
                text: '2. Não flexione o tronco (dobrar a coluna) quando abaixar para pegar uma carga.'
            MDLabel:
                text: '3. Sempre que for movimentar uma carga a distâncias maiores que 2 metros, utilize um carrinho ou empilhadeira.'
            MDLabel:
                text: '4. Sempre que for levantar uma carga cujo peso seja maior que 15 kg, peça ajuda a um colega.'
            MDLabel:
                text: '5. Evite levantar cargas torcendo o tronco para os lados.'
            MDLabel:
                text: '6. Respeite pausas entre um levantamento e outro, o ideal é manter a frequência de 1 levantamento a cada 5 minutos.'
            MDLabel:
                text: '7. Não eleve cargas acima do nível da cabeça.'
            MDLabel:
                text: '8. Sempre que for levantar ou movimentar uma carga, mantenha uma postura de base: pernas afastadas umas das outras, joelhos semi flexionados, coluna ereta, braços próximos ao corpo (braços na vertical).'
            MDLabel:
                text: '9. Na movimentação de carrinhos, prefira empurrar ao invés de puxar.'
            MDLabel:
                text: '10. Quando estiver movimentando cargas instáveis (bombonas, sacos, ou recipientes com líquido), onde o baricentro se desloca, redobre a atenção quanto a sua postura.'

<TerceiraImagem>:

    name: 'terceira_imagem'
    MDBoxLayout:
        orientation: 'vertical'
        
        MDTopAppBar:
            elevation: 2
            left_action_items: [['arrow-left', lambda x: app.guia_postural_press()]]
        MDBoxLayout:
            orientation: 'vertical'
            MDLabel:
                text: '1- Mouse e teclado posicionados em linha reta ajudam a se preservar de movimentos repetitivos ao oscilar entre um e outro; '
            MDLabel:
                text: '2- Para o uso de notebooks '
            MDLabel:
                text: '3- Caso haja teclado e mouse extras, o notebook pode ser posicionado no suporte ou sobre algum objeto, como, livros e revistas, como base. A tela deve ficar na linha dos olhos; '
            MDLabel:
                text: '4- As articulações precisam ficar na angulação de 90°, bem como a coluna deve se manter reta; '
            MDLabel:
                text: '5- O notebook deve ficar posicionado de maneira que os antebraços fiquem com a maior área possível sobre a superfície e que os pulsos não fiquem apoiados na borda da mesa.'

<QuartaImagem>:
    name: 'quarta_imagem'
    MDBoxLayout:
        orientation: 'vertical'
        
        MDTopAppBar:
            elevation: 2
            left_action_items: [['arrow-left', lambda x: app.guia_postural_press()]]
        MDBoxLayout:
            orientation: 'vertical'

            MDLabel:
                text: '1- Alterne a posição da mão e reveze os dedos'
            MDLabel:
                text: '2- Use a opção hands-free sempre que possível'
            MDLabel:
                text: '3- Evite excesso de força ao segurar o celular'
            MDLabel:
                text: '4- Mantenha boa postura ao olhar para a tela'
            MDLabel:
                text: '5- Manter o pescoço ereto e evitar flexionar muito os braços. Resumindo: leve o celular até a altura dos olhos e não o contrário.'

<ExercicioLaboral>:
    name: 'exercicio_laboral'
    MDBoxLayout:
        
        md_bg_color: 'lightblue'
        orientation: 'vertical'
        MDTopAppBar:
            md_bg_color: 0,0,0,0
            elevation: 0
            title: 'Exercício Laboral'
            anchor_title: 'left'
            type_height: 'small'
            left_action_items: [['arrow-left', lambda x: app.voltar()]]
            right_action_items: [['arrow-right-bold', lambda x: app.ex1()]]
        MDBoxLayout:
            
            orientation: 'vertical'
            size_hint_y:.75
            cols:2
            padding:[dp(15),dp(15),dp(15),dp(35)]
            spacing:dp(15)
            
            MDCard:
                ripple_behavior: True
                on_release: app.ex1()
                MDFloatLayout:
                    AsyncImage:
                        source: 'ex1.gif'
                        pos_hint: {'center_x': .08, 'center_y': .5}
                        anim_delay: 1/1
                
                    
            MDCard: 
                ripple_behavior: True
                on_release: app.ex2()

                MDFloatLayout:
                    AsyncImage:
                        source: 'ex2.gif'
                        pos_hint: {'center_x': .08, 'center_y': .5}
                        anim_delay: 1/1

            MDCard:
                ripple_behavior: True
                on_release: app.ex3()
                MDFloatLayout:
                    AsyncImage:
                        source: 'ex3.gif'  
                        pos_hint: {'center_x': .08, 'center_y': .5}
                        anim_delay: 1/1
      
                    
            MDCard:
                ripple_behavior: True
                on_release: app.ex4()
                MDFloatLayout:
                    AsyncImage:
                        source: 'ex4.gif'   
                        pos_hint: {'center_x': .08, 'center_y': .5}
                        anim_delay: 1/1
                        
            MDCard:
                ripple_behavior: True
                on_release: app.ex5()
                MDFloatLayout:
                    AsyncImage:
                        source: 'ex5.gif'
                        pos_hint: {'center_x': .05, 'center_y': .5}
                        anim_delay: 1/1
                 
                
           
            MDCard:
                ripple_behavior: True
                on_release: app.ex6()
                MDFloatLayout:
                    AsyncImage:
                        source: 'ex6.gif'  
                        pos_hint: {'center_x': .05, 'center_y': .5}
                        anim_delay: 1/1
    
            MDCard:
                ripple_behavior: True
                on_release: app.ex7()
                MDFloatLayout:
                    AsyncImage:
                        source: 'ex7.gif'
                        pos_hint: {'center_x': .08, 'center_y': .5}
                        anim_delay: 1/1

<Exercicio1>:
    name: 'exercicio1'
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            left_action_items: [['arrow-left', lambda x: app.ex_laboral()]]
            title: 'Exercício'
            anchor_title: 'center'
            elevation: 0
        
        MDFloatLayout:
            AsyncImage:
                source: 'ex1.gif'
                pos_hint: {'center_x': .5, 'center_y': .7}
                anim_delay: 1/1
            MDFillRoundFlatIconButton:
                text: 'PRÓXIMO!'
                font_size: '18sp'
                pos_hint: {'center_x': .5, 'center_y': .15}
                size_hint: .5, .1
                on_release: app.ex2()
            MDIconButton:
                icon: 'chevron-right-circle'
                pos_hint: {'center_x': .9, 'center_y': .15}
                icon_size: '50sp'
                theme_icon_color: "Custom"
                icon_color: 'blue'
                on_release: app.ex2()

            MDLabel:
                text: 'NOME'
                pos_hint: {'center_x': .95, 'center_y': .4}
                font_size: '18sp'
            MDLabel:
                text: '1 REP X 45 SEC'
                pos_hint: {'center_x': .85, 'center_y': .3}
                font_size: '18sp'

<Exercicio2>:
    name: 'exercicio2'
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            left_action_items: [['arrow-left', lambda x: app.ex_laboral()]]
            title: 'Exercício'
            anchor_title: 'center'
            elevation: 0
        
        MDFloatLayout:
            AsyncImage:
                source: 'ex2.gif'
                pos_hint: {'center_x': .5, 'center_y': .7}
                anim_delay: 1/1
            MDFillRoundFlatIconButton:
                text: 'PRÓXIMO!'
                font_size: '18sp'
                pos_hint: {'center_x': .5, 'center_y': .15}
                size_hint: .5, .1
                on_release: app.ex3()
            MDIconButton:
                icon: 'chevron-right-circle'
                pos_hint: {'center_x': .9, 'center_y': .15}
                icon_size: '50sp'
                theme_icon_color: "Custom"
                icon_color: 'blue'
                on_release: app.ex3()
            MDIconButton:
                icon: 'chevron-left-circle'
                pos_hint: {'center_x': .1, 'center_y': .15}
                icon_size: '50sp'
                theme_icon_color: "Custom"
                icon_color: 'blue'
                on_release: app.ex1()
            MDLabel:
                text: 'NOME'
                pos_hint: {'center_x': .95, 'center_y': .4}
                font_size: '18sp'
            MDLabel:
                text: '1 REP X 45 SEC'
                pos_hint: {'center_x': .85, 'center_y': .3}
                font_size: '18sp'

<Exercicio3>:
    name: 'exercicio3'
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            left_action_items: [['arrow-left', lambda x: app.ex_laboral()]]
            title: 'Exercício'
            anchor_title: 'center'
            elevation: 0
        
        MDFloatLayout:
            AsyncImage:
                source: 'ex3.gif'
                pos_hint: {'center_x': .5, 'center_y': .7}
                anim_delay: 1/1
            MDFillRoundFlatIconButton:
                text: 'PRÓXIMO!'
                font_size: '18sp'
                pos_hint: {'center_x': .5, 'center_y': .15}
                size_hint: .5, .1
                on_release: app.ex4()
            MDIconButton:
                icon: 'chevron-right-circle'
                pos_hint: {'center_x': .9, 'center_y': .15}
                icon_size: '50sp'
                theme_icon_color: "Custom"
                icon_color: 'blue'
                on_release: app.ex4()
            MDIconButton:
                icon: 'chevron-left-circle'
                pos_hint: {'center_x': .1, 'center_y': .15}
                icon_size: '50sp'
                theme_icon_color: "Custom"
                icon_color: 'blue'
                on_release: app.ex2()
            MDLabel:
                text: 'NOME'
                pos_hint: {'center_x': .95, 'center_y': .4}
                font_size: '18sp'
            MDLabel:
                text: '1 REP X 45 SEC'
                pos_hint: {'center_x': .85, 'center_y': .3}
                font_size: '18sp'              

<Exercicio4>:
    name: 'exercicio4'
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            left_action_items: [['arrow-left', lambda x: app.ex_laboral()]]
            title: 'Exercício'
            anchor_title: 'center'
            elevation: 0
        
        MDFloatLayout:
            AsyncImage:
                source: 'ex4.gif'
                pos_hint: {'center_x': .5, 'center_y': .7}
                anim_delay: 1/1
            MDFillRoundFlatIconButton:
                text: 'PRÓXIMO!'
                font_size: '18sp'
                pos_hint: {'center_x': .5, 'center_y': .15}
                size_hint: .5, .1
                on_release: app.ex5()
            MDIconButton:
                icon: 'chevron-right-circle'
                pos_hint: {'center_x': .9, 'center_y': .15}
                icon_size: '50sp'
                theme_icon_color: "Custom"
                icon_color: 'blue'
                on_release: app.ex5()
            MDIconButton:
                icon: 'chevron-left-circle'
                pos_hint: {'center_x': .1, 'center_y': .15}
                icon_size: '50sp'
                theme_icon_color: "Custom"
                icon_color: 'blue'
                on_release: app.ex3()
            MDLabel:
                text: 'NOME'
                pos_hint: {'center_x': .95, 'center_y': .4}
                font_size: '18sp'
            MDLabel:
                text: '1 REP X 45 SEC'
                pos_hint: {'center_x': .85, 'center_y': .3}
                font_size: '18sp'

<Exercicio5>:
    name: 'exercicio5'
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            left_action_items: [['arrow-left', lambda x: app.ex_laboral()]]
            title: 'Exercício'
            anchor_title: 'center'
            elevation: 0
        
        MDFloatLayout:
            AsyncImage:
                source: 'ex5.gif'
                pos_hint: {'center_x': .5, 'center_y': .7}
                anim_delay: 1/1
            MDFillRoundFlatIconButton:
                text: 'PRÓXIMO!'
                font_size: '18sp'
                pos_hint: {'center_x': .5, 'center_y': .15}
                size_hint: .5, .1
                on_release: app.ex6()
            MDIconButton:
                icon: 'chevron-right-circle'
                pos_hint: {'center_x': .9, 'center_y': .15}
                icon_size: '50sp'
                theme_icon_color: "Custom"
                icon_color: 'blue'
                on_release: app.ex6()
            MDIconButton:
                icon: 'chevron-left-circle'
                pos_hint: {'center_x': .1, 'center_y': .15}
                icon_size: '50sp'
                theme_icon_color: "Custom"
                icon_color: 'blue'
                on_release: app.ex4()
            MDLabel:
                text: 'NOME'
                pos_hint: {'center_x': .95, 'center_y': .4}
                font_size: '18sp'
            MDLabel:
                text: '1 REP X 45 SEC'
                pos_hint: {'center_x': .85, 'center_y': .3}
                font_size: '18sp'

<Exercicio6>:
    name: 'exercicio6'
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            left_action_items: [['arrow-left', lambda x: app.ex_laboral()]]
            title: 'Exercício'
            anchor_title: 'center'
            elevation: 0
        
        MDFloatLayout:
            AsyncImage:
                source: 'ex6.gif'
                pos_hint: {'center_x': .5, 'center_y': .7}
                anim_delay: 1/1
                size_hint: .7, .7
            MDFillRoundFlatIconButton:
                text: 'PRÓXIMO!'
                font_size: '18sp'
                pos_hint: {'center_x': .5, 'center_y': .15}
                size_hint: .5, .1
                on_release: app.ex7()
            MDIconButton:
                icon: 'chevron-right-circle'
                pos_hint: {'center_x': .9, 'center_y': .15}
                icon_size: '50sp'
                theme_icon_color: "Custom"
                icon_color: 'blue'
                on_release: app.ex7()
            MDIconButton:
                icon: 'chevron-left-circle'
                pos_hint: {'center_x': .1, 'center_y': .15}
                icon_size: '50sp'
                theme_icon_color: "Custom"
                icon_color: 'blue'
                on_release: app.ex5()
            MDLabel:
                text: 'NOME'
                pos_hint: {'center_x': .95, 'center_y': .4}
                font_size: '18sp'
            MDLabel:
                text: '1 REP X 45 SEC'
                pos_hint: {'center_x': .85, 'center_y': .3}
                font_size: '18sp'

<Exercicio7>:
    name: 'exercicio7'
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            left_action_items: [['arrow-left', lambda x: app.ex_laboral()]]
            title: 'Exercício'
            anchor_title: 'center'
            elevation: 0
        
        MDFloatLayout:
        
            AsyncImage:
                source: 'ex7.gif'
                pos_hint: {'center_x': .5, 'center_y': .7}
                anim_delay: 1/1
            MDFillRoundFlatIconButton:
                text: 'CONCLUIR!'
                font_size: '18sp'
                pos_hint: {'center_x': .5, 'center_y': .15}
                size_hint: .5, .1
                on_release: app.ex_laboral()
            MDIconButton:
                icon: 'chevron-right-circle'
                pos_hint: {'center_x': .9, 'center_y': .15}
                icon_size: '50sp'
                theme_icon_color: "Custom"
                icon_color: 'blue'
                on_release: app.ex_laboral()
            MDIconButton:
                icon: 'chevron-left-circle'
                pos_hint: {'center_x': .1, 'center_y': .15}
                icon_size: '50sp'
                theme_icon_color: "Custom"
                icon_color: 'blue'
                on_release: app.ex6()
            MDLabel:
                text: 'NOME'
                pos_hint: {'center_x': .95, 'center_y': .4}
                font_size: '18sp'
            MDLabel:
                text: '1 REP X 45 SEC'
                pos_hint: {'center_x': .85, 'center_y': .3}
                font_size: '18sp'

<Insatisfacao>:
    name: 'insatisfacao'
    MDScrollView:
        MDBoxLayout:
            md_bg_color: 'blue'
            orientation:'vertical'
            MDTopAppBar:
                left_action_items: [['arrow-left', lambda x: app.voltar()]]
                title: 'Insatisfações'
                anchor_title: 'center'
                elevation: 0
            
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
                    on_release: app.other()
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
                            
                            text: 'Outros'
                            
                            pos_hint: {'center_x': .3, 'center_y': .6}

<Outros>:
    name: 'outros'
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            left_action_items: [['arrow-left', lambda x: app.insa()]]
            title: 'Outros'
            anchor_title: 'center'
            elevation: 0
        MDBoxLayout:
            MDFloatLayout:
                MDTextField:
                    hint_text: "Digite sua insatifação"
                    mode: "rectangle"
                    size_hint: .8, .5
                    pos_hint: {'center_x': .5, 'center_y': .7}
                    multiline: True
                MDRaisedButton:
                    text: 'Enviar'
                    pos_hint: {'center_x': .8, 'center_y': .4}

<FaleConosco>:
    name: 'fale_conosco'
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            left_action_items: [['arrow-left', lambda x: app.voltar()]]
            title: 'Fale Conosco'
            anchor_title: 'center'
            elevation: 0
        MDBoxLayout:
            MDFloatLayout:
                MDTextField:
                    hint_text: "Fale conosco"
                    mode: "rectangle"
                    size_hint: .8, .5
                    pos_hint: {'center_x': .5, 'center_y': .7}
                    multiline: True
                MDRaisedButton:
                    text: 'Enviar'
                    pos_hint: {'center_x': .8, 'center_y': .4}

<Questionario>:
    name: 'questionario'
    MDBoxLayout:
        
        md_bg_color: 'blue'
        orientation: 'vertical'
        MDTopAppBar:
            left_action_items: [['arrow-left', lambda x: app.voltar()]]
            title: 'Questionário'
            anchor_title: 'center'
            elevation: 0
        MDBoxLayout:
            size_hint_y:.75
            cols:2
            padding:[dp(15),dp(15),dp(15),dp(35)]
            spacing:dp(15)
            orientation: 'vertical'
            MDCard:
                on_release: app.mental()
                padding:dp(10)
                spacing:dp(10)
                radius:dp(25)
                ripple_behavior: True
                MDFloatLayout:
                MDFloatLayout:    
                    MDLabel:
                        adaptive_size: True
                        text: 'Exigência mental'
                        
                        pos_hint: {'center_x': .01, 'center_y': .6}

            MDCard:
                on_release: app.fisica()
                padding:dp(10)
                spacing:dp(10)
                radius:dp(25)
                ripple_behavior: True
                MDFloatLayout:
                MDFloatLayout:    
                    MDLabel:
                        adaptive_size: True
                        text: 'Exigência física'
                        
                        pos_hint: {'center_x': .01, 'center_y': .6}
            MDCard:
                on_release: app.temporal()
                padding:dp(10)
                spacing:dp(10)
                radius:dp(25)
                ripple_behavior: True
                MDFloatLayout:
                MDFloatLayout:    
                    MDLabel:
                        adaptive_size: True
                        text: 'Exigência temporal'
                        
                        pos_hint: {'center_x': .01, 'center_y': .6}
            MDCard:
                on_release: app.esforco()
                padding:dp(10)
                spacing:dp(10)
                radius:dp(25)
                ripple_behavior: True
                MDFloatLayout:
                MDFloatLayout:    
                    MDLabel:
                        adaptive_size: True
                        text: 'Nível de esforço'
                        
                        pos_hint: {'center_x': .01, 'center_y': .6}
            MDCard:
                on_release: app.frustracao()
                padding:dp(10)
                spacing:dp(10)
                radius:dp(25)
                ripple_behavior: True
                MDFloatLayout:
                MDFloatLayout:    
                    MDLabel:
                        adaptive_size: True
                        text: 'Nível de frustração'
                        
                        pos_hint: {'center_x': .01, 'center_y': .6}
            MDCard:
                on_release: app.realizacao()
                padding:dp(10)
                spacing:dp(10)
                radius:dp(25)
                ripple_behavior: True
                MDFloatLayout:
                MDFloatLayout:    
                    MDLabel:
                        adaptive_size: True
                        text: 'Nível de realização'
                        
                        pos_hint: {'center_x': .01, 'center_y': .6}

        

<ExigenciaMental>:
    name: 'exigencia_mental'       
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: 'blue'     
        MDTopAppBar:
            left_action_items: [['arrow-left', lambda x: app.quest()]]
            title: 'Exigência mental'
            anchor_title: 'center'
            elevation: 0
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
                MDFloatLayout:    
                    MDLabel:
                        adaptive_size: True
                        text: 'PERFEITO'
                        
                        pos_hint: {'center_x': .01, 'center_y': .6}
            MDCard:
                
                padding:dp(10)
                spacing:dp(10)
                radius:dp(25)
                ripple_behavior: True
                MDFloatLayout:
                MDFloatLayout:    
                    MDLabel:
                        adaptive_size: True
                        text: 'MUITO BOM'
                        
                        pos_hint: {'center_x': .01, 'center_y': .6}
            MDCard:
                
                padding:dp(10)
                spacing:dp(10)
                radius:dp(25)
                ripple_behavior: True
                MDFloatLayout:
                MDFloatLayout:    
                    MDLabel:
                        adaptive_size: True
                        text: 'BOM'
                        
                        pos_hint: {'center_x': .01, 'center_y': .6}
            MDCard:
                
                padding:dp(10)
                spacing:dp(10)
                radius:dp(25)
                ripple_behavior: True
                MDFloatLayout:
                MDFloatLayout:    
                    MDLabel:
                        adaptive_size: True
                        text: 'COMPLICADO'
                        
                        pos_hint: {'center_x': .01, 'center_y': .6}
            MDCard:
                
                padding:dp(10)
                spacing:dp(10)
                radius:dp(25)
                ripple_behavior: True
                MDFloatLayout:
                MDFloatLayout:    
                    MDLabel:
                        adaptive_size: True
                        text: 'DIFÍCIL'
                        
                        pos_hint: {'center_x': .01, 'center_y': .6}


<ExigenciaFisica>:
    name: 'exigencia_fisica'
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: 'blue'     
        MDTopAppBar:
            left_action_items: [['arrow-left', lambda x: app.quest()]]
            title: 'Exigência física'
            anchor_title: 'center'
            elevation: 0
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
                MDFloatLayout:    
                    MDLabel:
                        adaptive_size: True
                        text: 'PERFEITO'
                        
                        pos_hint: {'center_x': .01, 'center_y': .6}
            MDCard:
                
                padding:dp(10)
                spacing:dp(10)
                radius:dp(25)
                ripple_behavior: True
                MDFloatLayout:
                MDFloatLayout:    
                    MDLabel:
                        adaptive_size: True
                        text: 'MUITO BOM'
                        
                        pos_hint: {'center_x': .01, 'center_y': .6}
            MDCard:
                
                padding:dp(10)
                spacing:dp(10)
                radius:dp(25)
                ripple_behavior: True
                MDFloatLayout:
                MDFloatLayout:    
                    MDLabel:
                        adaptive_size: True
                        text: 'BOM'
                        
                        pos_hint: {'center_x': .01, 'center_y': .6}
            MDCard:
                
                padding:dp(10)
                spacing:dp(10)
                radius:dp(25)
                ripple_behavior: True
                MDFloatLayout:
                MDFloatLayout:    
                    MDLabel:
                        adaptive_size: True
                        text: 'COMPLICADO'
                        
                        pos_hint: {'center_x': .01, 'center_y': .6}
            MDCard:
                
                padding:dp(10)
                spacing:dp(10)
                radius:dp(25)
                ripple_behavior: True
                MDFloatLayout:
                MDFloatLayout:    
                    MDLabel:
                        adaptive_size: True
                        text: 'DIFÍCIL'
                        
                        pos_hint: {'center_x': .01, 'center_y': .6}

<ExigenciaTemporal>:
    name: 'exigencia_temporal'
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: 'blue'     
        MDTopAppBar:
            left_action_items: [['arrow-left', lambda x: app.quest()]]
            title: 'Exigência temporal'
            anchor_title: 'center'
            elevation: 0
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
                MDFloatLayout:    
                    MDLabel:
                        adaptive_size: True
                        text: 'PERFEITO'
                        
                        pos_hint: {'center_x': .01, 'center_y': .6}
            MDCard:
                
                padding:dp(10)
                spacing:dp(10)
                radius:dp(25)
                ripple_behavior: True
                MDFloatLayout:
                MDFloatLayout:    
                    MDLabel:
                        adaptive_size: True
                        text: 'MUITO BOM'
                        
                        pos_hint: {'center_x': .01, 'center_y': .6}
            MDCard:
                
                padding:dp(10)
                spacing:dp(10)
                radius:dp(25)
                ripple_behavior: True
                MDFloatLayout:
                MDFloatLayout:    
                    MDLabel:
                        adaptive_size: True
                        text: 'BOM'
                        
                        pos_hint: {'center_x': .01, 'center_y': .6}
            MDCard:
                
                padding:dp(10)
                spacing:dp(10)
                radius:dp(25)
                ripple_behavior: True
                MDFloatLayout:
                MDFloatLayout:    
                    MDLabel:
                        adaptive_size: True
                        text: 'COMPLICADO'
                        
                        pos_hint: {'center_x': .01, 'center_y': .6}
            MDCard:
                
                padding:dp(10)
                spacing:dp(10)
                radius:dp(25)
                ripple_behavior: True
                MDFloatLayout:
                MDFloatLayout:    
                    MDLabel:
                        adaptive_size: True
                        text: 'DIFÍCIL'
                        
                        pos_hint: {'center_x': .01, 'center_y': .6}


<NivelEsforco>:
    name: 'nivel_esforco'
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: 'blue'     
        MDTopAppBar:
            left_action_items: [['arrow-left', lambda x: app.quest()]]
            title: 'Nível de esforço'
            anchor_title: 'center'
            elevation: 0
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
                MDFloatLayout:    
                    MDLabel:
                        adaptive_size: True
                        text: 'PERFEITO'
                        
                        pos_hint: {'center_x': .01, 'center_y': .6}
            MDCard:
                
                padding:dp(10)
                spacing:dp(10)
                radius:dp(25)
                ripple_behavior: True
                MDFloatLayout:
                MDFloatLayout:    
                    MDLabel:
                        adaptive_size: True
                        text: 'MUITO BOM'
                        
                        pos_hint: {'center_x': .01, 'center_y': .6}
            MDCard:
                
                padding:dp(10)
                spacing:dp(10)
                radius:dp(25)
                ripple_behavior: True
                MDFloatLayout:
                MDFloatLayout:    
                    MDLabel:
                        adaptive_size: True
                        text: 'BOM'
                        
                        pos_hint: {'center_x': .01, 'center_y': .6}
            MDCard:
                
                padding:dp(10)
                spacing:dp(10)
                radius:dp(25)
                ripple_behavior: True
                MDFloatLayout:
                MDFloatLayout:    
                    MDLabel:
                        adaptive_size: True
                        text: 'COMPLICADO'
                        
                        pos_hint: {'center_x': .01, 'center_y': .6}
            MDCard:
                
                padding:dp(10)
                spacing:dp(10)
                radius:dp(25)
                ripple_behavior: True
                MDFloatLayout:
                MDFloatLayout:    
                    MDLabel:
                        adaptive_size: True
                        text: 'DIFÍCIL'
                        
                        pos_hint: {'center_x': .01, 'center_y': .6}

<NivelFrustracao>:
    name: 'nivel_frustracao'
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: 'blue'     
        MDTopAppBar:
            left_action_items: [['arrow-left', lambda x: app.quest()]]
            title: 'Nível de frustração'
            anchor_title: 'center'
            elevation: 0
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
                MDFloatLayout:    
                    MDLabel:
                        adaptive_size: True
                        text: 'PERFEITO'
                        
                        pos_hint: {'center_x': .01, 'center_y': .6}
            MDCard:
                
                padding:dp(10)
                spacing:dp(10)
                radius:dp(25)
                ripple_behavior: True
                MDFloatLayout:
                MDFloatLayout:    
                    MDLabel:
                        adaptive_size: True
                        text: 'MUITO BOM'
                        
                        pos_hint: {'center_x': .01, 'center_y': .6}
            MDCard:
                
                padding:dp(10)
                spacing:dp(10)
                radius:dp(25)
                ripple_behavior: True
                MDFloatLayout:
                MDFloatLayout:    
                    MDLabel:
                        adaptive_size: True
                        text: 'BOM'
                        
                        pos_hint: {'center_x': .01, 'center_y': .6}
            MDCard:
                
                padding:dp(10)
                spacing:dp(10)
                radius:dp(25)
                ripple_behavior: True
                MDFloatLayout:
                MDFloatLayout:    
                    MDLabel:
                        adaptive_size: True
                        text: 'COMPLICADO'
                        
                        pos_hint: {'center_x': .01, 'center_y': .6}
            MDCard:
                
                padding:dp(10)
                spacing:dp(10)
                radius:dp(25)
                ripple_behavior: True
                MDFloatLayout:
                MDFloatLayout:    
                    MDLabel:
                        adaptive_size: True
                        text: 'DIFÍCIL'
                        
                        pos_hint: {'center_x': .01, 'center_y': .6}

<NivelRealizacao>:
    name: 'nivel_realizacao'
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: 'blue'     
        MDTopAppBar:
            left_action_items: [['arrow-left', lambda x: app.quest()]]
            title: 'Nível de realização'
            anchor_title: 'center'
            elevation: 0
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
                MDFloatLayout:    
                    MDLabel:
                        adaptive_size: True
                        text: 'PERFEITO'
                        
                        pos_hint: {'center_x': .01, 'center_y': .6}
            MDCard:
                
                padding:dp(10)
                spacing:dp(10)
                radius:dp(25)
                ripple_behavior: True
                MDFloatLayout:
                MDFloatLayout:    
                    MDLabel:
                        adaptive_size: True
                        text: 'MUITO BOM'
                        
                        pos_hint: {'center_x': .01, 'center_y': .6}
            MDCard:
                
                padding:dp(10)
                spacing:dp(10)
                radius:dp(25)
                ripple_behavior: True
                MDFloatLayout:
                MDFloatLayout:    
                    MDLabel:
                        adaptive_size: True
                        text: 'BOM'
                        
                        pos_hint: {'center_x': .01, 'center_y': .6}
            MDCard:
                
                padding:dp(10)
                spacing:dp(10)
                radius:dp(25)
                ripple_behavior: True
                MDFloatLayout:
                MDFloatLayout:    
                    MDLabel:
                        adaptive_size: True
                        text: 'COMPLICADO'
                        
                        pos_hint: {'center_x': .01, 'center_y': .6}
            MDCard:
                
                padding:dp(10)
                spacing:dp(10)
                radius:dp(25)
                ripple_behavior: True
                MDFloatLayout:
                MDFloatLayout:    
                    MDLabel:
                        adaptive_size: True
                        text: 'DIFÍCIL'
                        
                        pos_hint: {'center_x': .01, 'center_y': .6}
        
''')

class JanelaGerenciadora(ScreenManager):
    pass

class JanelaPrincipal(Screen):
    pass

class Cadastro(Screen):
    pass

class Janela1(Screen):
    pass

class GuiaPostural(Screen):
    pass

class PrimeiraImagem(Screen):
    pass

class SegundaImagem(Screen):
    pass

class TerceiraImagem(Screen):
    pass

class QuartaImagem(Screen):
    pass

class ExercicioLaboral(Screen):
    pass

class Exercicio1(Screen):
    pass

class Exercicio2(Screen):
    pass

class Exercicio3(Screen):
    pass

class Exercicio4(Screen):
    pass

class Exercicio5(Screen):
    pass

class Exercicio6(Screen):
    pass

class Exercicio7(Screen):
    pass

class Insatisfacao(Screen):
    pass

class Outros(Screen):
    pass

class FaleConosco(Screen):
    pass

class Questionario(Screen):
    pass

class ExigenciaMental(Screen):
    pass

class ExigenciaFisica(Screen):
    pass

class ExigenciaTemporal(Screen):
    pass

class NivelEsforco(Screen):
    pass

class NivelFrustracao(Screen):
    pass

class NivelRealizacao(Screen):
    pass

class MyApp(MDApp):
    
    def voltar_login(self):
        self.janela_gerenciadora.current = 'janela_principal'

    def voltar(self):
        self.janela_gerenciadora.current = 'janela1'
        
    def guia1(self):
        self.janela_gerenciadora.current = 'primeira_imagem'

    def guia2(self):
        self.janela_gerenciadora.current = 'segunda_imagem'
    
    def guia3(self):
        self.janela_gerenciadora.current = 'terceira_imagem'

    def guia4(self):
        self.janela_gerenciadora.current = 'quarta_imagem'

    def ex_laboral(self):
        self.janela_gerenciadora.current = 'exercicio_laboral'
    
    def change_color(self):
        theme = self.theme_cls.theme_style
        if theme == 'Dark':
            self.theme_cls.theme_style = 'Light'
        else:
            self.theme_cls.theme_style = 'Dark'

    def guia_postural_press(self):
        self.janela_gerenciadora.current = 'guia_postural'
    
    def ex1(self):
        self.janela_gerenciadora.current = 'exercicio1'

    def ex2(self):
        self.janela_gerenciadora.current = 'exercicio2'

    def ex3(self):
        self.janela_gerenciadora.current = 'exercicio3'

    def ex4(self):
        self.janela_gerenciadora.current = 'exercicio4'

    def ex5(self):
        self.janela_gerenciadora.current = 'exercicio5'

    def ex6(self):
        self.janela_gerenciadora.current = 'exercicio6'

    def ex7(self):
        self.janela_gerenciadora.current = 'exercicio7'

    def insa(self):
        self.janela_gerenciadora.current = 'insatisfacao'

    def other(self):
        self.janela_gerenciadora.current = 'outros'

    def faleConosco(self):
        self.janela_gerenciadora.current = 'fale_conosco'

    def quest(self):
        self.janela_gerenciadora.current = 'questionario'

    def mental(self):
        self.janela_gerenciadora.current = 'exigencia_mental'

    def fisica(self):
        self.janela_gerenciadora.current = 'exigencia_fisica'

    def temporal(self):
        self.janela_gerenciadora.current = 'exigencia_temporal'

    def esforco(self):
        self.janela_gerenciadora.current = 'nivel_esforco'

    def frustracao(self):
        self.janela_gerenciadora.current = 'nivel_frustracao'

    def realizacao(self):
        self.janela_gerenciadora.current = 'nivel_realizacao'


    def build(self):
        
        self.theme_cls.primary_palette = 'Blue'
        self.janela_gerenciadora = JanelaGerenciadora()
        self.janela_principal = JanelaPrincipal()
        self.janela1 = Janela1()
        self.cadastro = Cadastro()
        self.guia_postural = GuiaPostural()
        self.primeira_imagem = PrimeiraImagem()
        self.segunda_imagem = SegundaImagem()
        self.terceira_imagem = TerceiraImagem()
        self.quarta_imagem = QuartaImagem()
        self.exercicio_laboral = ExercicioLaboral()
        self.exercicio1 = Exercicio1()
        self.exercicio2 = Exercicio2()
        self.exercicio3 = Exercicio3()
        self.exercicio4 = Exercicio4()
        self.exercicio5 = Exercicio5()
        self.exercicio6 = Exercicio6()
        self.exercicio7 = Exercicio7()
        self.insatisfacao = Insatisfacao()
        self.outros = Outros()
        self.fale_conosco = FaleConosco()
        self.questionario = Questionario()
        self.exigencia_mental = ExigenciaMental()
        self.exigencia_fisica = ExigenciaFisica()
        self.exigencia_temporal= ExigenciaTemporal()
        self.nivel_esforco = NivelEsforco()
        self.nivel_frustracao = NivelFrustracao()
        self.nivel_realizacao = NivelRealizacao()
        self.janela_gerenciadora.add_widget(self.janela_principal)
        self.janela_gerenciadora.add_widget(self.cadastro)
        self.janela_gerenciadora.add_widget(self.janela1)
        self.janela_gerenciadora.add_widget(self.guia_postural)
        self.janela_gerenciadora.add_widget(self.primeira_imagem)
        self.janela_gerenciadora.add_widget(self.segunda_imagem)
        self.janela_gerenciadora.add_widget(self.terceira_imagem)
        self.janela_gerenciadora.add_widget(self.quarta_imagem)
        self.janela_gerenciadora.add_widget(self.exercicio_laboral)
        self.janela_gerenciadora.add_widget(self.exercicio1)
        self.janela_gerenciadora.add_widget(self.exercicio2)
        self.janela_gerenciadora.add_widget(self.exercicio3)
        self.janela_gerenciadora.add_widget(self.exercicio4)
        self.janela_gerenciadora.add_widget(self.exercicio5)
        self.janela_gerenciadora.add_widget(self.exercicio6)
        self.janela_gerenciadora.add_widget(self.exercicio7)
        self.janela_gerenciadora.add_widget(self.insatisfacao)
        self.janela_gerenciadora.add_widget(self.outros)
        self.janela_gerenciadora.add_widget(self.fale_conosco)
        self.janela_gerenciadora.add_widget(self.questionario)
        self.janela_gerenciadora.add_widget(self.exigencia_mental)
        self.janela_gerenciadora.add_widget(self.exigencia_fisica)
        self.janela_gerenciadora.add_widget(self.exigencia_temporal)
        self.janela_gerenciadora.add_widget(self.nivel_esforco)
        self.janela_gerenciadora.add_widget(self.nivel_frustracao)
        self.janela_gerenciadora.add_widget(self.nivel_realizacao)
        
        return self.janela_gerenciadora
    
MyApp().run()