#!/usr/bin/env python3

from pathlib import Path
from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast

from kivy.core.text import LabelBase
from kivymd.font_definitions import theme_font_styles


class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Window.bind(on_keyboard=self.events)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            preview=False,
            selector='file',
            ext=['.py']
        )
        print(self.theme_cls.font_styles)

    def build(self):
        screen = Screen()
        return screen

    def file_manager_open(self):
        self.file_manager.show('/')  # entry point of browser
        self.manager_open = True

    def select_path(self, path):
        '''It will be called when you click on the file name
        or the catalog selection button.

        :type path: str;
        :param path: path to the selected directory or file;
        '''

        self.exit_manager()
        label = self.root.ids.firmware_path
        loader_button = self.root.ids.loader_button

        loader_button.disabled = False
        label.text = self.get_absolute_path(path)
        self.firmware_path = path
        toast(path)

    def exit_manager(self, *args):
        '''Called when the user reaches the root of the directory tree.'''

        self.manager_open = False
        self.file_manager.close()

    def get_absolute_path(self, path):
        p = Path(path)
        return p.resolve().__str__()


    """
    def events(self, instance, keyboard, keycode, text, modifiers):
        '''Called when buttons are pressed on the mobile device.'''

        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True"""


MainApp().run()
