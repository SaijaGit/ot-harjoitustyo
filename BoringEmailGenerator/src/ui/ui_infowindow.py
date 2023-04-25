from tkinter import ttk, Toplevel, constants
import tkinter as tk
from .styles import configure_main_window_styles, bg_colour


class InfoWindow:
    def __init__(self, title, info_text, button1_text, button2_text,  button1_func, button2_func):
        self.window = Toplevel()
        self.window.title(title)
        self.button1_text = button1_text
        self.button2_text = button2_text
        self.button1_func = button1_func
        self.button2_func = button2_func
        self.window.configure(bg=bg_colour)
        self.window.geometry("600x100")

        self.window.grid_rowconfigure((0, 1, 2, 3), weight=0)
        self.window.grid_columnconfigure((0, 1, 2, 3), weight=1)

        configure_main_window_styles()

        self.info_text = ttk.Label(self.window, text=info_text)
        self.info_text.config(font=("Georgia", 10, "bold"),
                              background=bg_colour)
        self.info_text.grid(row=0, column=0, columnspan=4, pady=15)

        if button1_text is not None:
            self.draw_buttons()

    def draw_buttons(self):

        self.left_button = ttk.Button(
            master=self.window, text=self.button1_text, style='Delete.TButton', command=self.button1_handler)
        self.left_button.grid(row=1, column=1, columnspan=1,
                              padx=5, pady=10, sticky=(constants.E, constants.W))

        self.right_button = ttk.Button(
            master=self.window, text=self.button2_text, style='Copy.TButton', command=self.button2_handler)
        self.right_button.grid(row=1, column=2, columnspan=1,
                               padx=5, pady=10, sticky=(constants.E, constants.W))

    def button1_handler(self):
        if self.button1_func is None:
            self.window.withdraw()
        else:
            self.button1_func

    def button2_handler(self):
        if self.button2_func is None:
            self.window.withdraw()
        else:
            self.button2_func

    def close(self):
        self.window.withdraw()

    def show(self):
        self.window.deiconify()

    def hide(self):
        self.hide()
