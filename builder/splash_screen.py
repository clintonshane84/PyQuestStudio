from dearpygui.core import *
from dearpygui.dearpygui import start_dearpygui
from dearpygui.simple import *
import time
import threading
import os
from PIL import Image

# Duration before main window opens
SPLASH_DURATION = 2.5  # seconds

# Path to splash image
SPLASH_IMAGE_PATH = os.path.join("assets", "ui", "splash.png")

def show_main_window():
    delete_item("SplashWindow")
    import builder.main_window  # triggers creation of main UI

def launch_main_delayed():
    time.sleep(SPLASH_DURATION)
    show_main_window()


def set_window_pos(param, x, y):
    pass


def create_splash_screen():
    # Load image dimensions using Pillow
    image = Image.open(SPLASH_IMAGE_PATH)
    width, height = image.size

    # Load image into DearPyGui
    add_additional_font("assets/ui/OpenSans-SemiBold.ttf", 18, tag="default_font")  # Optional
    add_texture("splash_texture", *load_image(SPLASH_IMAGE_PATH))

    # Set window size to image size
    set_main_window_size(width, height)
    set_main_window_title("PyQuestStudio Loading...")

    # Center window (estimates for 1080p screen — adjust or make dynamic if needed)
    screen_width = 1920
    screen_height = 1080
    x = int((screen_width - width) / 2)
    y = int((screen_height - height) / 2)

    with window("SplashWindow", no_title_bar=True, no_resize=True, no_move=True, no_close=True):
        add_image("splash_texture")

    set_window_pos("SplashWindow", x, y)

    # Trigger transition after delay
    threading.Thread(target=launch_main_delayed, daemon=True).start()
    start_dearpygui(primary_window="SplashWindow")

# Helper to load an image into a DearPyGui-compatible format
def load_image(path):
    image = Image.open(path).convert("RGBA")
    width, height = image.size
    raw_data = image.tobytes("raw", "RGBA", 0, -1)
    return width, height, [int(b)/255.0 for b in raw_data]

if __name__ == "__main__":
    create_splash_screen()
