from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView


class Tarefas(ScrollView):
    #Define o metodo de inicialização da classe
    def __init__(self,tarefas, **kwargs):
        super().__init__(**kwargs)  #--> chama o metodo de inicialização do Super(BoxLayout)
        for tarefa in tarefas:
            self.ids.box.add_widget(Label(text=tarefa, font_size=30, size_hint_y =None, height=200))


class Test(App):
    def build(self):
        return Tarefas(['Fazer compras', 'Buscar filho', 'Buscar filho', 'Buscar filho', 'Buscar filho', 'Buscar filho'])


if __name__ == '__main__':
    Test().run()