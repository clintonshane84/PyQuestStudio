import time
import threading
import os
from PIL import Image
import dearpygui.dearpygui as dpg

# Duration before main window opens
SPLASH_DURATION = 2.5  # seconds

# Path to splash image
SPLASH_IMAGE_PATH = os.path.join("assets", "ui", "splash.png")


def show_main_window():
    dpg.delete_item("SplashWindow")
    import builder.main_window  # Launches the main window GUI


def launch_main_delayed():
    time.sleep(SPLASH_DURATION)
    show_main_window()


def load_image_texture(path: str):
    """Loads image as RGBA texture for use in DearPyGui."""
    image = Image.open(path).convert("RGBA")
    width, height = image.size
    data = image.tobytes("raw", "RGBA", 0, -1)
    texture_data = [v / 255 for v in data]

    with dpg.texture_registry(show=False):
        dpg.add_static_texture(width, height, texture_data, tag="splash_texture")

    return width, height


def create_splash_screen():
    dpg.create_context()

    # Load splash image and register as texture
    width, height = load_image_texture(SPLASH_IMAGE_PATH)

    dpg.create_viewport(title='PyQuestStudio Loading...', width=width, height=height)
    dpg.setup_dearpygui()

    with dpg.window(tag="SplashWindow", no_title_bar=True, no_resize=True, no_move=True, no_close=True,
                    no_scrollbar=True):
        dpg.add_image("splash_texture")

    # Center the viewport (optional basic center approximation)
    screen_width = 1920  # For dynamic resolution you'd need OS-specific code
    screen_height = 1080
    x = int((screen_width - width) / 2)
    y = int((screen_height - height) / 2)
    dpg.set_viewport_pos((x, y))

    dpg.show_viewport()

    # Launch main window in background thread
    threading.Thread(target=launch_main_delayed, daemon=True).start()

    dpg.start_dearpygui()
    dpg.destroy_context()


if __name__ == "__main__":
    create_splash_screen()
