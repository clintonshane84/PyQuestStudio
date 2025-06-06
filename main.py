from dearpygui.core import *
from dearpygui.simple import *

def create_main_window():
    set_main_window_size(1200, 800)
    set_main_window_title("PyQuestStudio")

    with window("MainWindow"):
        add_text("Welcome to PyQuestStudio!")
        # Later we’ll add docked panels, scene canvas, etc.

create_main_window()
