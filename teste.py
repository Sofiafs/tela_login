from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen

class TelaLogin(BoxLayout):
    def __init__ (self, **kwargs):
        super(TelaLogin, self).__init__(**kwargs)
        self.orientation= "vertical"
        self.padding= [50, 20]
        self.spacing= 10

        Window.clearcolor= (0, 0, 0.1, 1)
        self.add_widget(Image(source='/Users/aluno.sesipaulista/Documents/Login/img/imagem.png'))

        self.add_widget(Label(text='L O G I N', font_size=30, bold=True))

        self.username_input= TextInput(hint_text='Digite o usuário...', multiline=False, size_hint=(None, None), size=(900, 70))
        self.password_input= TextInput(hint_text='Digite a senha...',password=True,multiline=False, size_hint=(None, None), size=(900, 70))
        self.add_widget(self.username_input)
        self.add_widget(self.password_input)

        self.buttons_layout= BoxLayout(padding=[0, 10], spacing=10)
        self.login_button= Button(text='Entrar', color=(0, 0, 0.1, 1), size_hint=(None, None), size=(450, 50),background_color =(100, 100, 100, 100))
        self.login_button.bind(on_press=self.login)
        self.signup_button= Button(text='Cadastre-se', color=(0, 0, 0.1, 1), size_hint=(None,None), size=(450, 50),background_color =(100, 100, 100, 100), on_press=self.ir_para_segunda_tela)
        self.buttons_layout.add_widget(self.login_button)
        self.buttons_layout.add_widget(self.signup_button)
        self.add_widget(self.buttons_layout)
        
    def ir_para_segunda_tela(self, *args):
        self.manager.current = 'Cadastro'

    def login(self,instance):
        username = self.username_input.text
        password= self.password_input.text
        print('Username:', username)
        print('Password:', password)

class MyApp(App):
    def build(self):
        return TelaLogin()
    
if __name__ == '_main_':
    MyApp().run()
    

    
    
    
    
    
    
class TelaCadastro(BoxLayout):
    def __init__ (self, **kwargs):
        super(TelaCadastro, self).__init__(**kwargs)
        self.orientation= "vertical"
        self.padding= [50, 20]
        self.spacing= 10

        Window.clearcolor= (0, 0, 0.1, 1)

        self.add_widget(Label(text='C A D A S T R O', font_size=30, bold=True))


        self.name_input= TextInput(hint_text='Digite o seu nome...', multiline=False, size_hint=(None, None), size=(900, 70))
        self.email_input= TextInput(hint_text='Digite o seu e-mail...', multiline=False, size_hint=(None, None), size=(900, 70))
        self.number_input= TextInput(hint_text='Digite o seu número de telefone...', multiline=False, size_hint=(None, None), size=(900, 70))
        self.password_input= TextInput(hint_text='Digite a sua senha...', password=True, size_hint=(None, None), size=(900, 70))
        self.add_widget(self.name_input)
        self.add_widget(self.password_input)
        self.add_widget(self.email_input)
        self.add_widget(self.number_input)

        self.buttons_layout= BoxLayout(padding=[0, 10], spacing=10)
        self.signup_button= Button(text='Cadastrar', color=(0, 0, 0.1, 1), size_hint=(None,None), size=(900, 50),background_color =(100, 100, 100, 100))
        self.buttons_layout.add_widget(self.signup_button)
        self.add_widget(self.buttons_layout)

    def cadastro(self,instance):
        password= self.password_input.text
        nome= self.name_input.text
        email= self.email_input.text
        numero= self.number_input.text
        print('Password:', password)
        print('Nome:', nome)
        print('E-mail:', email)
        print('Número:', numero)

class MyApp(App):
    def build(self):
        return TelaCadastro()

class TestApp(App):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(TelaLogin(name='login'))
        screen_manager.add_widget(TelaCadastro(name='cadastro'))
        return screen_manager
    
if __name__ == '__main__':
    MyApp().run()


class TelaCadastro(BoxLayout, TelaLogin):
    def __init__ (self, **kwargs):
        super(TelaCadastro, self).__init__(**kwargs)
        self.orientation= "vertical"
        self.padding= [50, 20]
        self.spacing= 10

        Window.clearcolor= (0, 0, 0.1, 2)
        
        self.add_widget(Label(text='C A D A S T R O', font_size=23))


        self.user_layout = BoxLayout(padding=[0, 10], spacing=10)
        self.username_label = Label(text="  N O M E:", font_size=20)
        self.username_input = TextInput(hint_text='Digite aqui...', multiline=False)
        self.user_layout.add_widget(self.username_label)
        self.user_layout.add_widget(self.username_input)
        self.add_widget(self.user_layout)

        self.user_layout2 = BoxLayout(padding=[0, 10], spacing=10)
        self.email_label = Label(text="  E - M A I L:", font_size=20)
        self.email_input = TextInput(hint_text='Digite aqui...', multiline=False)
        self.user_layout2.add_widget(self.email_label)
        self.user_layout2.add_widget(self.email_input)
        self.add_widget(self.user_layout2)

        self.user_layout3 = BoxLayout(padding=[0, 10], spacing=10)
        self.fone_label = Label(text="  C E L U L A R:", font_size=20)
        self.fone_input = TextInput(hint_text='Digite aqui...', multiline=False)
        self.user_layout3.add_widget(self.fone_label)
        self.user_layout3.add_widget(self.fone_input)
        self.add_widget(self.user_layout3)

        self.user_layout4 = BoxLayout(padding=[0, 10], spacing=10)
        self.senha_label = Label(text="  S E N H A:", font_size=20)
        self.senha_input = TextInput(hint_text='Digite aqui...', multiline=False)
        self.user_layout4.add_widget(self.senha_label)
        self.user_layout4.add_widget(self.senha_input)
        self.add_widget(self.user_layout4)

        self.buttons_layout4= BoxLayout(padding=[0, 10], spacing=10)
        self.signup_button= Button(text='c a d a s t r e - s e',color=(0, 0, 0, 1), size_hint=(None,None), size=(920, 50), background_color =(100, 100, 100, 100))
        self.signup_button.bind(on_press=self.TelaLogin)
        self.buttons_layout4.add_widget(self.signup_button)
        self.add_widget(self.buttons_layout4)

    def cadastro(self,instance):
        username = self.username_input.text
        email= self.email_input.text
        numero= self.fone_input.text
        password = self.senha_input.text
        print('Username:', username)
        print('E-mail:', email)
        print('Password:', password)
        print('Número:', numero)