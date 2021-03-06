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
from kivy.animation import Animation
from kivy.core.audio import SoundLoader
import json

class GrenciadorTelas(ScreenManager):
    pass

class Menu(Screen):
    def on_pre_enter(self):
        Window.bind(on_request_close=self.confirmacao)


    def confirmacao(self, *args, **kwargs):
        global popSound
        popSound.play()
        box = BoxLayout(orientation='vertical', padding='5sp', spacing='10sp')
        botoes = BoxLayout(padding=30*0.3, spacing=10*0.5)
        pop = Popup(title="Deseja sair?", content=box, size_hint=(None, None),
                    size=('200dp', '150dp'))

        sim = BotaoCustomizado(text="Sim", on_release=App.get_running_app().stop)
        nao = BotaoCustomizado(text="Nao", on_release=pop.dismiss)
        atencao = Image(source='Image/warn.png')

        botoes.add_widget(sim)
        botoes.add_widget(nao)

        box.add_widget(atencao)
        box.add_widget(botoes)

        animText = Animation(color=(0.3,0.3,0.3,1), duration=1.5) + Animation(color=(1,1,1,1), duration=1.5)
        animText.repeat = True
        animText.start(sim)
        anim = Animation(size=(400, 300), duration=0.1, t='out_back')
        anim.start(pop)
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

    def on_cor(self, *args):
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

class Configuracao(Screen):
    configs = []

    def on_pre_enter(self):
        self.load_config()

    def save_config(self):
        with open('config.json','w') as config:
            json.dump(self.configs, config)

    def load_config(self):
        try:
            with open('config.json', 'r') as config:
                self.ids.slider.value = json.load(config)*200
        except FileNotFoundError:
            pass

    def volume(self,volume,*args):
        popSound.volume = volume/200
        poppapSound.volume = volume/200
        self.configs = popSound.volume



class Tarefas(Screen):
    tarefas = []
    path = ''
    popSound = None
    poppapSound = None

    def on_pre_enter(self):
        self.ids.box.clear_widgets()
        self.path = App.get_running_app().user_data_dir+'/'
        self.load_data_tarefas()
        Window.bind(on_keyboard=self.voltar)
        Window.bind(on_keyboard=self.adicionar_tarefa)
        self.ids.texto.focus=True
        for tarefa in self.tarefas:
            self.ids.box.add_widget(Tarefa(text=tarefa))


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

    def load_data_tarefas(self, *args):
        try:
            with open(self.path+'data.json', 'r') as data:
                self.tarefas = json.load(data)
        except FileNotFoundError:
            pass

    def save_data_tarefas(self):
        with open(self.path+'data.json','w') as data:
            json.dump(self.tarefas, data)

    def remove_widget_tarefas(self,tarefa):
        global poppapSound
        poppapSound.play()
        texto = tarefa.ids.label.text
        self.ids.box.remove_widget(tarefa)
        self.tarefas.remove(texto)
        self.save_data_tarefas()

    def add_widget_tarefas(self):
        global popSound
        popSound.play()
        texto = self.ids.texto.text
        if texto.strip():
            self.ids.box.add_widget(Tarefa(text=texto))
            self.ids.texto.text = ''
            self.tarefas.append(texto)
            self.save_data_tarefas()




class Tarefa(BoxLayout):
    def __init__(self,text='', **kwargs):
        super().__init__(**kwargs)
        self.ids.label.text = text


class Test(App):
    def build(self):
        return GrenciadorTelas()

popSound = SoundLoader.load('sound/pop_alert.mp3')
poppapSound = SoundLoader.load('sound/long_pop.wav')
popSound.volume = 1
poppapSound.volume = 1


if __name__ == '__main__':
    Test().run()