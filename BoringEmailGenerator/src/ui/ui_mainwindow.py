from tkinter import Tk, ttk, constants, scrolledtext #, clipboard_append, clipboard_clear
from repositories.message_db import MessageDB


bg_colour = "#bbe1fa"


class UI:
    
    def __init__(self, root, database):
        self._root = root
        self._message_entry = None
        self._root.configure(bg=bg_colour)


        self._database = database
        self.group_names = self._database.get_groups()
        self.message_texts = []
        for i in range(1,9) :
            self.message_texts.append(self._database.messages_by_group(i))




    def start(self):
        header1_label = ttk.Label(master=self._root, text="Boring Email Generator")
        header1_label.config(font=("Georgia", 30, "bold"), background=bg_colour)
        header1_label.grid(row=0, column=0, columnspan=4, pady=15)


        comboboxes = []

        for i in range(8):
            combobox = ttk.Combobox(master=self._root, values=self.message_texts[i])
            combobox.set(self.group_names[i])
            
            combobox.bind('<<ComboboxSelected>>', self._handle_comboboxes)

            if i < 4 : row = 1
            else : row = 2
            column = i%4
            combobox.grid(row=row, column=column, columnspan=1, padx=5, pady=5)
            comboboxes.append(combobox)



        self._message_entry = scrolledtext.ScrolledText(master=self._root, height=20)
        self._message_entry.grid(row=3, column=0, columnspan=4, sticky=(constants.E, constants.W), padx=15, pady=15)



        delete_button_style = ttk.Style()
        delete_button_style.theme_use('default')
        delete_button_style.configure('Delete.TButton', padding=6, relief="flat", font=('Georgia', 12, 'bold'), background='#cc2b5b', foreground='black')
        delete_button_style.map('Delete.TButton', background=[('active', '#fa2039'), ('disabled', '#ba2d3d')], foreground=[('pressed', '#361317'), ('active', 'black')])
        delete_button = ttk.Button(master=self._root, text="Delete", style='Delete.TButton', command=lambda: self._message_entry.delete('1.0', 'end')) #self._handle_delete_button_click)

        copy_button_style = ttk.Style()
        copy_button_style.theme_use('default')
        copy_button_style.configure('Copy.TButton', padding=6, relief="flat", font=('Georgia', 12, 'bold'), background='#2bcc3b', foreground='black')
        copy_button_style.map('Copy.TButton', background=[('active', '#3ed643'), ('disabled', '#30ab34')], foreground=[('pressed', '#04170f'), ('active', 'black')])
        copy_button = ttk.Button(master=self._root, text="Copy", style='Copy.TButton', command=self._handle_copy_button_click)

        delete_button.grid(row=4, column=2, columnspan=1,  padx=5, pady=5, sticky=(constants.E, constants.W))
        copy_button.grid(row=4, column=3, columnspan=1,  padx=5, pady=5, sticky=(constants.E, constants.W))

        self._root.grid_columnconfigure((0,1,2,3), weight=1)


    def _handle_comboboxes(self, event):
        combobox = event.widget
        value = combobox.get()
        print(f"COMBOBOX!! Value of entry is: {value}")
        self._message_entry.insert('end', value)



    def _handle_copy_button_click(self):
        entry_value = self._message_entry.get('1.0', 'end-1c')
        print(f"COPY-BUTTON!! Value of entry is: {entry_value}")
        self._root.clipboard_clear()
        self._root.clipboard_append(entry_value)

