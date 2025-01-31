from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class OutfitGrid(GridLayout):
    
    def __init__(self):
        super(OutfitGrid, self).__init__()


class MainApp(App):
    
    def build(self):
        return OutfitGrid()

MainApp().run()