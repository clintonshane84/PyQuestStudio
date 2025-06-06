import dearpygui.dearpygui as dpg

def create_main_window():
    dpg.create_context()

    dpg.create_viewport(title="PyQuestStudio", width=1200, height=800)
    dpg.setup_dearpygui()

    with dpg.window(tag="MainWindow"):
        dpg.add_text("Welcome to PyQuestStudio!")
        # Later we’ll add docked panels, scene canvas, etc.

    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()

if __name__ == "__main__":
    create_main_window()
