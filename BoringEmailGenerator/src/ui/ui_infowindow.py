from tkinter import ttk, Toplevel, constants
import tkinter as tk
from .styles import configure_main_window_styles, bg_colour


class InfoWindow:
    def __init__(self, root, title, info_text):
        self.window = Toplevel(root)
        self.window.transient()

        self.title = title
        self.text = info_text
        self.window.configure(bg=bg_colour)
        self.window.geometry("600x100")

        self.window.grid_rowconfigure((0, 1, 2, 3), weight=0)
        self.window.grid_columnconfigure((0, 1, 2, 3), weight=1)

        configure_main_window_styles()

        self.info_text = ttk.Label(self.window)
        self.info_text.config(font=("Georgia", 10, "bold"),
                              background=bg_colour)
        self.info_text.grid(row=0, column=0, columnspan=4, pady=15)

        self.draw_texts()
        self.window.protocol("WM_DELETE_WINDOW", self.close)
        self.window.withdraw()

        self.running = False

    def show(self):
        if self.running:
            return

        self.running = True
        self.window.deiconify()

        # while self.running:
        #    self.window.update_idletasks()
        #    self.window.update()
        #    self.window.after(100)

    def draw_texts(self):
        self.window.title(self.title)
        self.info_text.config(text=self.text)

    def destroy(self):
        self.window.destroy()

    def close(self):
        self.window.withdraw()

    def hide(self):
        self.hide()

    def update_contents(self, title, info_text):
        self.title = title
        self.text = info_text

        self.draw_texts()

        # self.window.deiconify()
# self.window.update_idletasks()
