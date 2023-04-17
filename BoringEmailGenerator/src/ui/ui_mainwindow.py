

from tkinter import Tk, ttk, constants, scrolledtext
# from ui_managementwindow import ManagementWindow
from repositories.db_messages import MessageDB
from .ui_managementwindow import ManagementWindow


bg_colour = "#bbe1fa"


class MainWindow:

    def __init__(self, root, message_handler):
        self._root = root
        self._message_entry = None
        self._root.configure(bg=bg_colour)

        self._message_handler = message_handler
        self.group_names = self._message_handler.group_name_list()
        self.message_texts = self._message_handler.all_message_texts_grouped()

        self._management_window = None

        self.comboboxes = []

    def start(self):

        self._root.grid_rowconfigure(0, weight=0)
        self._root.grid_rowconfigure(1, weight=0)
        self._root.grid_rowconfigure(2, weight=0)
        self._root.grid_rowconfigure(3, weight=0)
        self._root.grid_rowconfigure(4, weight=1)
        self._root.grid_rowconfigure(5, weight=0)

        self._draw_header1()

        self.draw_comboboxes()

        self._draw_modify_content_buttons()

        self._draw_textarea()

        self._draw_text_area_buttons()

        self._root.grid_columnconfigure((0, 1, 2, 3), weight=1)

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
            combobox_style = ttk.Style()
            combobox_style.configure('TCombobox', padding=(5, 2, 5, 2))
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

    def _draw_modify_content_buttons(self):

        manage_button_style = ttk.Style()
        manage_button_style.theme_use('default')
        manage_button_style.configure('Manage.TButton', padding=6, relief="flat", font=(
            'Georgia', 12, 'bold'), background='#6666cc', foreground='black')
        manage_button_style.map('Manage.TButton', background=[('active', '#bc5bf0'), (
            'disabled', '#8c8c8c')], foreground=[('pressed', '#000033'), ('active', 'black')])
        manage_button = ttk.Button(master=self._root, text="Modify templates",
                                   style='Manage.TButton', command=self._handle_management_window_button_click)

        manage_button.grid(row=3, column=3, columnspan=1,
                           padx=5, pady=10, sticky=(constants.E, constants.W))

    def _draw_textarea(self):
        self._message_entry = scrolledtext.ScrolledText(
            master=self._root, height=80, wrap="word")
        self._message_entry.grid(row=4, column=0, columnspan=4, sticky=(
            constants.E, constants.W), padx=15, pady=15)

    def _draw_text_area_buttons(self):

        delete_button_style = ttk.Style()
        delete_button_style.theme_use('default')
        delete_button_style.configure('Delete.TButton', padding=6, relief="flat", font=(
            'Georgia', 12, 'bold'), background='#cc2b5b', foreground='black')
        delete_button_style.map('Delete.TButton', background=[('active', '#de4831'), (
            'disabled', '#8c8c8c')], foreground=[('pressed', '#361317'), ('active', 'black')])
        delete_button = ttk.Button(master=self._root, text="Empty", style='Delete.TButton',
                                   command=lambda: self._message_entry.delete('1.0', 'end'))  # self._handle_delete_button_click)

        copy_button_style = ttk.Style()
        copy_button_style.theme_use('default')
        copy_button_style.configure('Copy.TButton', padding=6, relief="flat", font=(
            'Georgia', 12, 'bold'), background='#2bcc3b', foreground='black')
        copy_button_style.map('Copy.TButton', background=[('active', '#89e639'), (
            'disabled', '#8c8c8c')], foreground=[('pressed', '#04170f'), ('active', 'black')])
        copy_button = ttk.Button(master=self._root, text="Copy",
                                 style='Copy.TButton', command=self._handle_copy_button_click)

        delete_button.grid(row=5, column=2, columnspan=1,
                           padx=10, pady=10, sticky=(constants.W, constants.E))
        copy_button.grid(row=5, column=3, columnspan=1,  padx=10,
                         pady=10, sticky=(constants.E, constants.W))

    def _handle_comboboxes(self, event):
        combobox = event.widget
        value = combobox.get()
        print(f"COMBOBOX!! Value of entry is: {value}")
        combobox.set(combobox.group_name)
        self._message_entry.insert('end', value)
        self._message_entry.see("end-1c")
        self._message_entry.mark_set("insert", "end-1c")
        self._message_entry.focus_set()

    def _handle_copy_button_click(self):
        entry_value = self._message_entry.get('1.0', 'end-1c')
        print(f"COPY-BUTTON!! Value of entry is: {entry_value}")
        self._root.clipboard_clear()
        self._root.clipboard_append(entry_value)

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
