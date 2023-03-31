from tkinter import Tk, ttk, constants, scrolledtext #, clipboard_append, clipboard_clear


bg_colour = "#bbe1fa"
#bg_colour = "orange"

group1_name = "Group 1"
group2_name = "Group 2"
group3_name = "Group 3"
group4_name = "Group 4"
group5_name = "Group 5"
group6_name = "Group 6"
group7_name = "Group 7"
group8_name = "Group 8"


group1_values = ["Group 1 Value 1", "Group 1 Value 2", "Group 1 Value 3"]
group2_values = ["Group 2 Value 1", "Group 2 Value 2", "Group 2 Value 3"]
group3_values = ["Group 3 Value 1", "Group 3 Value 2", "Group 3 Value 3"]
group4_values = ["Group 4 Value 1", "Group 4 Value 2", "Group 4 Value 3"]
group5_values = ["Group 5 Value 1", "Group 5 Value 2", "Group 5 Value 3"]
group6_values = ["Group 6 Value 1", "Group 6 Value 2", "Group 6 Value 3"]
group7_values = ["Group 7 Value 1", "Group 7 Value 2", "Group 7 Value 3"]
group8_values = ["Group 8 Value 1", "Group 8 Value 2", "Group 8 Value 3"]


class UI:
    
    def __init__(self, root):
        self._root = root
        self._message_entry = None


    def start(self):
        header1_label = ttk.Label(master=self._root, text="Boring Email Generator")

        group1_combobox = ttk.Combobox(master=self._root, values = group1_values)
        group1_combobox.set(group1_name)
        group1_combobox.bind('<<ComboboxSelected>>', self._handle_group1_combobox)
        group2_combobox = ttk.Combobox(master=self._root, values = group2_values)
        group2_combobox.set(group2_name)
        group3_combobox = ttk.Combobox(master=self._root, values = group3_values)
        group3_combobox.set(group3_name)
        group4_combobox = ttk.Combobox(master=self._root, values = group4_values)
        group4_combobox.set(group4_name)
        group5_combobox = ttk.Combobox(master=self._root, values = group5_values)
        group5_combobox.set(group5_name)
        group6_combobox = ttk.Combobox(master=self._root, values = group6_values)
        group6_combobox.set(group6_name)
        group7_combobox = ttk.Combobox(master=self._root, values = group7_values)
        group7_combobox.set(group7_name)
        group8_combobox = ttk.Combobox(master=self._root, values = group8_values)
        group8_combobox.set(group8_name)




        self._message_entry = scrolledtext.ScrolledText(master=self._root, height=20)

        delete_button_style = ttk.Style()
        delete_button_style.theme_use('default')
        delete_button_style.configure('Delete.TButton', padding=6, relief="flat", font=('Arial', 12, 'bold'), background='#cc2b5b', foreground='black')
        delete_button_style.map('Delete.TButton', background=[('active', '#fa2039'), ('disabled', '#ba2d3d')], foreground=[('pressed', '#361317'), ('active', 'black')])
        delete_button = ttk.Button(master=self._root, text="Delete", style='Delete.TButton', command=lambda: self._message_entry.delete('1.0', 'end')) #self._handle_delete_button_click)

        copy_button_style = ttk.Style()
        copy_button_style.theme_use('default')
        copy_button_style.configure('Copy.TButton', padding=6, relief="flat", font=('Arial', 12, 'bold'), background='#2bcc3b', foreground='black')
        copy_button_style.map('Copy.TButton', background=[('active', '#3ed643'), ('disabled', '#30ab34')], foreground=[('pressed', '#04170f'), ('active', 'black')])
        copy_button = ttk.Button(master=self._root, text="Copy", style='Copy.TButton', command=self._handle_copy_button_click)



        header1_label.config(font=("Georgia", 30, "bold"), background=bg_colour)
        header1_label.grid(row=0, column=0, columnspan=4, pady=15)

        group1_combobox.grid(row=1, column=0, columnspan=1, padx=5, pady=5)
        group2_combobox.grid(row=1, column=1, columnspan=1, padx=5, pady=5)
        group3_combobox.grid(row=1, column=2, columnspan=1, padx=5, pady=5)
        group4_combobox.grid(row=1, column=3, columnspan=1, padx=5, pady=5)
        group5_combobox.grid(row=2, column=0, columnspan=1, padx=5, pady=5)
        group6_combobox.grid(row=2, column=1, columnspan=1, padx=5, pady=5)
        group7_combobox.grid(row=2, column=2, columnspan=1, padx=5, pady=5)
        group8_combobox.grid(row=2, column=3, columnspan=1, padx=5, pady=5)

        self._message_entry.grid(row=3, column=0, columnspan=4, sticky=(constants.E, constants.W), padx=15, pady=15)


        delete_button.grid(row=4, column=2, columnspan=1,  padx=5, pady=5, sticky=(constants.E, constants.W))
        copy_button.grid(row=4, column=3, columnspan=1,  padx=5, pady=5, sticky=(constants.E, constants.W))

        self._root.grid_columnconfigure((0,1,2,3), weight=1)


    def _handle_group1_combobox(self, event):
        widget = event.widget
        value = widget.get()
        print(f"COMBOBOX 1!! Value of entry is: {value}")
        self._message_entry.insert('end', value)



    def _handle_copy_button_click(self):
        entry_value = self._message_entry.get('1.0', 'end-1c')
        print(f"COPY-BUTTON!! Value of entry is: {entry_value}")
        window.clipboard_clear()
        window.clipboard_append(entry_value)

window = Tk()
window.title("Boring Email Generator")
window.configure(bg=bg_colour)
window.geometry('800x800')

ui = UI(window)
ui.start()

window.mainloop()
