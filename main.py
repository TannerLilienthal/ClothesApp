from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

class OutfitLayout(FloatLayout):
    
    def __init__(self):
        super(OutfitLayout, self).__init__()

        window_h = Window.height
        window_w = Window.width

        # top right
        self.add_widget(
            Button(
                text = ">",
                size_hint = (0.1, 0.05),
                pos = (2 * window_w / 3, window_h / 5)
            )
        )
        # top left
        self.add_widget(
            Button(
                text = "<",
                size_hint = (0.1, 0.05),
                pos = ((window_w / 3) - (window_w * 0.1), window_h / 5)
            )
        )
        # bottom right
        self.add_widget(
            Button(
                text = ">",
                size_hint = (0.1, 0.05),
                pos = (2 * window_w / 3, 3 * window_h / 5)
            )
        )
        # bottom left
        self.add_widget(
            Button(
                text = "<",
                size_hint = (0.1, 0.05),
                pos = ((window_w / 3) - (window_w * 0.1), 3 * window_h / 5)
            )
        )


class MainApp(App):
    
    def build(self):
        return OutfitLayout()

MainApp().run()