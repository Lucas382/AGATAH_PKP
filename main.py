from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window


class GrenciadorTelas(ScreenManager):
    pass


class Menu(Screen):
    pass


class Tarefas(Screen):
    #Define o metodo de inicialização da classe
    def __init__(self,tarefas=[], **kwargs):
        super().__init__(**kwargs)  #--> chama o metodo de inicialização do Super(BoxLayout)
        for tarefa in tarefas:
            self.ids.box.add_widget(Tarefa(text=tarefa))


    def on_pre_enter(self):
        Window.bind(on_keyboard=self.voltar)


    def voltar(self, window, key_pressed, *args):
        if key_pressed == 27:
            App.get_running_app().root.transition.direction = 'right'
            App.get_running_app().root.current = 'menu'
            return True


    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.voltar)


    def add_widget_tarefas(self):
        texto = self.ids.texto.text
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