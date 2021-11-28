from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen


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