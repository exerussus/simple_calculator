
from kivy.app import App

from kivy.config import Config
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


Config.set('graphics', 'resizable', 0)
Config.write()
Config.set('graphics', 'width', 350)
Config.write()
Config.set('graphics', 'height', 500)
Config.write()


class CalculatorApp(App):

    def clearing(self, instance):
        if instance.text == '<--':
            self.form_text = self.form_text[:-1]
            self.update_label()
        if instance.text == 'C':
            self.form_text = ''
            self.update_label()

    def update_label(self):
        if self.form_text == '':
            self.form_text = '0'
        self.lbl.text = self.form_text

    def add_number(self, instance):
        if self.form_text == '0':
            self.form_text = ''
        self.form_text += str(instance.text)
        self.update_label()


    def add_operation(self, instance):
        # self.formula = int(self.form_text)
        self.form_text += ' ' + str(instance.text) + ' '
        self.update_label()



    def calc(self):
        answer = int(self.form_text)
        self.form_text = self.form_text, '=', str(answer)
        self.update_label()



    def build(self):
        self.form_text = ''
        bl = BoxLayout(orientation='vertical', padding=5)
        gl = GridLayout(cols=4, spacing=1, size_hint=(1, .6))
        self.lbl = Label(text='0', font_size=40, halign='right', valign='bottom', size_hint=(1, .4), text_size=(400 - 80, 500 * .4 - 50))
        bl.add_widget(self.lbl)

        gl.add_widget(Button(text='<--', on_press=self.clearing))
        gl.add_widget(Button(text='C', on_press=self.clearing))
        gl.add_widget(Button(text='back'))
        gl.add_widget(Button(text='=', on_press=self.calc))

        gl.add_widget(Button(text='7', on_press=self.add_number))
        gl.add_widget(Button(text='8', on_press=self.add_number))
        gl.add_widget(Button(text='9', on_press=self.add_number))
        gl.add_widget(Button(text='*', on_press=self.add_operation))

        gl.add_widget(Button(text='4', on_press=self.add_number))
        gl.add_widget(Button(text='5', on_press=self.add_number))
        gl.add_widget(Button(text='6', on_press=self.add_number))
        gl.add_widget(Button(text='+', on_press=self.add_operation))

        gl.add_widget(Button(text='1', on_press=self.add_number))
        gl.add_widget(Button(text='2', on_press=self.add_number))
        gl.add_widget(Button(text='3', on_press=self.add_number))
        gl.add_widget(Button(text='-', on_press=self.add_operation))

        gl.add_widget(Button(text='√', on_press=self.add_operation))
        gl.add_widget(Button(text='0', on_press=self.add_number))
        gl.add_widget(Button(text='.', on_press=self.add_number))
        gl.add_widget(Button(text='/', on_press=self.add_operation))

        bl.add_widget(gl)
        return bl


CalculatorApp().run()
