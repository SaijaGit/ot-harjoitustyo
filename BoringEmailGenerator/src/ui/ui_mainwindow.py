from tkinter import Tk, ttk, constants, scrolledtext
from repositories.db_messages import MessageDB
from .ui_managementwindow import ManagementWindow
from message_translator import MessageTranslator
from .styles import configure_main_window_styles, bg_colour


class MainWindow:

    def __init__(self, root, message_handler):
        self._root = root
        self._message_entry = None
        self._root.configure(bg=bg_colour)

        self._message_handler = message_handler
        self.group_names = self._message_handler.group_name_list()
        self.message_texts = self._message_handler.all_message_texts_grouped()

        self.translator = MessageTranslator()
        self.translate_language_inputs = []

        self._management_window = None

        self.comboboxes = []

    def start(self):

        configure_main_window_styles()

        self._root.grid_rowconfigure((0, 1, 2, 3, 4, 6), weight=0)
        self._root.grid_rowconfigure(5, weight=1)
        self._root.grid_columnconfigure((0, 1, 2, 3), weight=1)

        self._draw_header1()

        self.draw_comboboxes()

        self._draw_translate_inputs()

        self._draw_modify_content_button()

        self._draw_textarea()

        self._draw_text_area_buttons()

    def _draw_header1(self):
        header1_label = ttk.Label(
            master=self._root, text="Boring Email Generator")
        header1_label.config(font=("Georgia", 30, "bold"),
                             background=bg_colour)
        header1_label.grid(row=0, column=0, columnspan=4, pady=15)

    def draw_comboboxes(self):

        for combobox_column in range(4):
            self._root.grid_columnconfigure(combobox_column, weight=1)

        for i in range(8):
            combobox = ttk.Combobox(
                master=self._root, values=self.message_texts[i], width=30, height=5, style='TCombobox')

            combobox.group_name = self.group_names[i]
            combobox.set(self.group_names[i])

            combobox.bind('<<ComboboxSelected>>', self._handle_comboboxes)

            if i < 4:
                row = 1
            else:
                row = 2
            column = i % 4

            combobox.grid(row=row, column=column, padx=10, pady=5, sticky="ew")
            self.comboboxes.append(combobox)

    def _draw_modify_content_button(self):

        manage_button = ttk.Button(master=self._root, text="Modify templates",
                                   style='Manage.TButton', command=self._handle_management_window_button_click)
        manage_button.grid(row=3, column=3, columnspan=1,
                           padx=5, pady=10, sticky=(constants.E, constants.W))

    def _draw_textarea(self):
        self._message_entry = scrolledtext.ScrolledText(
            master=self._root, height=80, wrap="word")
        self._message_entry.grid(row=5, column=0, columnspan=4, sticky=(
            constants.E, constants.W), padx=15, pady=15)

    def _draw_text_area_buttons(self):

        delete_button = ttk.Button(master=self._root, text="Empty", style='Delete.TButton',
                                   command=lambda: self._message_entry.delete('1.0', 'end'))  # self._handle_delete_button_click)

        copy_button = ttk.Button(master=self._root, text="Copy",
                                 style='Copy.TButton', command=self._handle_copy_button_click)

        delete_button.grid(row=6, column=2, columnspan=1,
                           padx=10, pady=10, sticky=(constants.W, constants.E))
        copy_button.grid(row=6, column=3, columnspan=1,  padx=10,
                         pady=10, sticky=(constants.E, constants.W))

    def _draw_translate_inputs(self):

        language_list = self.translator.get_language_list()
        combobox_style = ttk.Style()
        combobox_style.configure('TCombobox', padding=(5, 2, 5, 2))

        language_from_combobox = ttk.Combobox(
            master=self._root, values=language_list, width=30, height=5, style='TCombobox')
        language_from_combobox.set("Translate from")
        language_from_combobox.bind(
            '<<ComboboxSelected>>', self._handle_language_comboboxes)

        language_to_combobox = ttk.Combobox(
            master=self._root, values=language_list, width=30, height=5, style='TCombobox')
        language_to_combobox.set("Translate to")
        language_to_combobox.bind(
            '<<ComboboxSelected>>', self._handle_language_comboboxes)

        language_from_combobox.grid(
            row=4, column=1, padx=10, pady=5, sticky="ew")
        language_to_combobox.grid(
            row=4, column=2, padx=10, pady=5, sticky="ew")
        self.translate_language_inputs = [
            language_from_combobox, language_to_combobox]

        translate_button = ttk.Button(master=self._root, text="Translate",
                                      style='Translate.TButton', command=self._handle_translate_button_click)

        translate_button.grid(row=4, column=3, columnspan=1,
                              padx=10, pady=10, sticky=(constants.W, constants.E))

    def _handle_comboboxes(self, event):
        combobox = event.widget
        value = combobox.get()
        print(f"COMBOBOX!! Value of entry is: {value}")
        combobox.set(combobox.group_name)
        self._message_entry.insert('end', value)
        self._message_entry.see("end-1c")
        self._message_entry.mark_set("insert", "end-1c")
        self._message_entry.focus_set()

    def _handle_language_comboboxes(self, event):
        combobox = event.widget
        value = combobox.get()
        print(f"LANGUAGE COMBOBOX!! Value of entry is: {value}")

    def _handle_copy_button_click(self):
        entry_value = self._message_entry.get('1.0', 'end-1c')
        print(f"COPY BUTTON!! Value of entry is: {entry_value}")
        self._root.clipboard_clear()
        self._root.clipboard_append(entry_value)

    def _handle_translate_button_click(self):
        translate_from = self.translate_language_inputs[0].get()
        translate_to = self.translate_language_inputs[1].get()

        original_text = self._message_entry.get('1.0', 'end-1c')
        if original_text == "" or translate_from == "Translate from" or translate_to == "Translate to":
            print(f"LANGUAGE BUTTON!! No text! {original_text}")

        else:
            print(f"LANGUAGE BUTTON!! Value of entry is: {original_text}")
            translated_text = self.translator.translate_message(
                original_text, translate_from, translate_to)
            if translated_text is not None:
                self._message_entry.delete('1.0', 'end')
                self._message_entry.insert('1.0', translated_text)
                self._message_entry.mark_set("insert", "end-1c")
                self._message_entry.focus_set()

    def _handle_management_window_button_click(self):

        if self._management_window is None or not self._management_window.winfo_exists():
            self._management_window = ManagementWindow(
                self._root, self._message_handler, self.update_combobox_groups, self.update_combobox_contents)
            self._management_window.start()
        else:
            self._management_window.lift()

    def update_combobox_groups(self):
        self.group_names = self._message_handler.group_name_list()
        for i in range(8):
            self.comboboxes[i].set(self.group_names[i])

    def update_combobox_contents(self):
        self.message_texts = self._message_handler.all_message_texts_grouped()
        for i in range(8):
            self.comboboxes[i]['values'] = self.message_texts[i]
            self.comboboxes[i].set(self.group_names[i])
