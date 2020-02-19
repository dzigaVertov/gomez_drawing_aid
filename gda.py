import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scatter import Scatter
from kivy.uix.popup import Popup
from kivy.clock import Clock
import os
from time import sleep
import sys
from random import choice


class Root_widget(Scatter):
    def __init__(self, **kwargs):
        super(Root_widget, self).__init__(**kwargs)
        Clock.schedule_once(self.foto)
        self.count = 0
        Clock.schedule_interval(self.foto, 30)
        Clock.schedule_interval(self.crono, 1)

    def crono(self, dt):

        self.ids.cronometro.text = str(30 - self.count % 30)
        self.count += 1

    def foto(self, dt):

        self.ids.fotito.source = choice(files)


class gdaApp(App):
    def build(self):
        Window.bind(on_request_close=self.on_request_close)
        self.view = Root_widget()
        self.title = "GDA"
        return self.view

    def on_request_close(self, *args):

        self.text_popup(title='Práctica', text='Tiempo: ' +
                        str(self.view.count // 60) + 'minutos')

        return True

    def text_popup(self, title='', text=''):
        box = BoxLayout(orientation='vertical')
        box.add_widget(Label(text=text))
        bot = Button(text='OK')
        box.add_widget(bot)
        popup = Popup(title=title, content=box)
        popup.open()
        bot.bind(on_release=Window.close)


if __name__ == '__main__':
    args = sys.argv
    if len(args) != 2:
        exit()
    elif not os.path.isdir(args[1]):
        exit()

    files = [os.path.join(path, filename)
             for path, dirs, files in os.walk(args[1])
             for filename in files]
    gdaApp().run()
