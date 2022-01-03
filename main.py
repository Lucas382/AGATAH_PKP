from kivy.app import App
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.properties import ListProperty
from kivy.uix.popup import Popup
from kivy.uix.image import Image

class GrenciadorTelas(ScreenManager):
    pass


class Menu(Screen):
    def on_pre_enter(self):
        Window.bind(on_request_close=self.confirmacao)

    def confirmacao(self, *args, **kwargs):
        box = BoxLayout(orientation='vertical', padding=5, spacing=10)
        botoes = BoxLayout(padding=40, spacing=10)
        pop = Popup(title="Deseja sair?", content=box, size_hint=(None, None),
                    size=(400, 300))

        sim = BotaoCustomizado(text="Sim", on_release=App.get_running_app().stop)
        nao = BotaoCustomizado(text="Nao", on_release=pop.dismiss)
        atencao = Image(source='Image/warn.png')

        botoes.add_widget(sim)
        botoes.add_widget(nao)

        box.add_widget(atencao)
        box.add_widget(botoes)

        pop.open()
        return True


class BotaoCustomizado(ButtonBehavior, Label):
    cor = ListProperty([0.5, 0.5, 0.5, 1])
    cor_press = ListProperty([0.3, 0.3, 0.3, 1])
    def __init__(self, **kwargs):
        super(BotaoCustomizado, self).__init__(**kwargs)
        self.atualizar()

    def on_pos(self, *args):
        self.atualizar()

    def on_size(self, *args):
        self.atualizar()

    def on_press(self, *args):
        self.cor, self.cor_press = self.cor_press, self.cor

    def on_release(self, *args):
        self.cor, self.cor_press  = self.cor_press, self.cor

    def on_cor(self,*args):
        self.atualizar()

    def atualizar(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(rgba=self.cor)
            Ellipse(size=(self.height, self.height),
                    pos=self.pos)
            Ellipse(size=(self.height, self.height),
                    pos=(self.x + self.width-self.height, self.y))
            Rectangle(size=(self.width-self.height, self.height),
                      pos=(self.x+self.height/2.0, self.y))


class Tarefas(Screen):
    #Define o metodo de inicialização da classe
    def __init__(self,tarefas=[], **kwargs):
        super().__init__(**kwargs)  #--> chama o metodo de inicialização do Super(BoxLayout)
        for tarefa in tarefas:
            self.ids.box.add_widget(Tarefa(text=tarefa))

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.voltar)
        Window.bind(on_keyboard=self.adicionar_tarefa)
        self.ids.texto.focus=True

    def voltar(self, window, key_pressed, *args):
        if key_pressed == 27: #Key: Escape
            App.get_running_app().root.transition.direction = 'right'
            App.get_running_app().root.current = 'menu'
            return True

    def adicionar_tarefa(self,window, key_pressed, *args):
        if key_pressed == 13: #Key: Return
            self.add_widget_tarefas()
            self.ids.texto.focus = True

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.voltar)

    def add_widget_tarefas(self):
        texto = self.ids.texto.text
        if texto.strip():
            self.ids.box.add_widget(Tarefa(text=texto))
            self.ids.texto.text = ''




class Tarefa(BoxLayout):
    def __init__(self,text='', **kwargs):
        super().__init__(**kwargs)
        self.ids.label.text = text


class Test(App):
    def build(self):
        return GrenciadorTelas()


if __name__ == '__main__':
    Test().run()