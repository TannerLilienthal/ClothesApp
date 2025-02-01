from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

class OutfitLayout(FloatLayout):
    
    def __init__(self):
        super(OutfitLayout, self).__init__()

        window_h = Window.height
        window_w = Window.width

        self.add_widget(
            Button(
                text = ">",
                size_hint = (0.1, 0.1),
                pos = (window_w / 2, window_h / 2)
            )
        )



class MainApp(App):
    
    def build(self):
        return OutfitLayout()

MainApp().run()