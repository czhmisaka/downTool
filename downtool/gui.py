from dearpygui import core, simple
<<<<<<< HEAD
from downtool import down as dt
=======
from downtool import down 
>>>>>>> c9b66416b8ace9f3b78132b14feb17ea126670fb

def save_callback(sender, data):
    print("Save Clicked")

<<<<<<< HEAD
with simple.window("name"):
=======
with simple.window("Example Window"):
    core.add_text("Hello world")
>>>>>>> c9b66416b8ace9f3b78132b14feb17ea126670fb
    core.add_button("Save", callback=save_callback)
    core.add_input_text("string")
    core.add_slider_float("float")

<<<<<<< HEAD
# core.start_dearpygui()


class Gui(dt):
    def __init__(self):
        super(Gui, self).__init__()
        self.window = simple.window
        self.core = core
        self.simple = simple
    
    
=======
core.start_dearpygui()
>>>>>>> c9b66416b8ace9f3b78132b14feb17ea126670fb
