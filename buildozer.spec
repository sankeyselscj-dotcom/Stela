from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class StelaNexusApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        layout.add_widget(Label(text='STELA NEXUS', font_size='30sp', bold=True))
        layout.add_widget(Label(text='App funcionando com sucesso! 🚀', font_size='18sp'))
        btn = Button(text='CLIQUE AQUI', size_hint=(1, 0.3), background_color=(0.2, 0.6, 1, 1))
        btn.bind(on_press=lambda x: print("Funcionou!"))
        layout.add_widget(btn)
        return layout

StelaNexusApp().run()
