from dearpygui import core, simple
from downtool import down as dt

def save_callback(sender, data):
    print("Save Clicked")

with simple.window("name"):
    core.add_button("Save", callback=save_callback)
    core.add_input_text("string")
    core.add_slider_float("float")

# core.start_dearpygui()


class Gui(dt):
    def __init__(self):
        super(Gui, self).__init__()
        self.window = simple.window
        self.core = core
        self.simple = simple
    
    