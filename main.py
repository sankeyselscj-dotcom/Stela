from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

class TelaInicial(Screen): pass
class TelaNexus(Screen): pass
class Gerenciador(ScreenManager): pass

class StelaApp(App):
    def build(self):
        Builder.load_file("stela.kv")
        return Gerenciador()

StelaApp().run()
