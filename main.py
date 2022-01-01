from kivy.app import App
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.graphics import  Color, Ellipse, Rectangle

class GrenciadorTelas(ScreenManager):
    pass


class Menu(Screen):
    pass

class BotaoCustomizado(ButtonBehavior, Label):
    def __init__(self, **kwargs):
        super(BotaoCustomizado, self).__init__(**kwargs)
        self.atualizar()

    def on_pos(self, *args):
        self.atualizar()

    def on_size(self, *args):
        self.atualizar()

    def atualizar(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(rgba=(0.5, 0.5, 0.5, 1))
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