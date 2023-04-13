from tkinter import Tk, ttk, Toplevel, constants, scrolledtext

bg_colour = "#bbe1fa"

class ManagementWindow(Toplevel):
    def __init__(self, master=None, database=None):
        super().__init__(master)

        self._root = master
        self.title("Manage Message Templates")
        self.geometry("800x600")
        

        #self._root.configure(bg=bg_colour)
        self.configure(bg=bg_colour)

        self._database = database
        self.group_names = self._database.get_groups()
        self.message_texts = self._database.all_messages_grouped()

        self.group_name_entries = []
        

    def start(self):

        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), weight=0)
        self.grid_columnconfigure((0, 1, 2, 3), weight=1)
        
        self._draw_header1()

        self._draw_header2()

        for i in range(8) :
            self._draw_header3((i), self.group_names[i])
            self._draw_group_name_entry(i)
            self._draw_group_name_button(i)





    def _draw_header1(self):
        header1_label = ttk.Label(
            master=self, text="Boring Email Generator")
        header1_label.config(font=("Georgia", 30, "bold"),
                             background=bg_colour)
        header1_label.grid(row=0, column=0, columnspan=4, pady=15)

    def _draw_header2(self):
        header2_label = ttk.Label(
            master=self, text="Modify templates")
        header2_label.config(font=("Georgia", 20, "bold"),
                             background=bg_colour)
        header2_label.grid(row=1, column=0, columnspan=1, pady=15)

    def _draw_header3(self, header3_id, text):
        header3_label = ttk.Label(
            master=self, text=f"Group #{header3_id+1}: {text}")
        header3_label.config(font=("Georgia", 15, "bold"),
                             background=bg_colour)
        header3_label.grid(row=header3_id+2, column=0, columnspan=1, pady=15)

    def _draw_group_name_entry(self, entry_id):
        group_name_entry = ttk.Entry(master=self)
        group_name_entry.config(font=("Georgia", 15, "bold"),
                             background=bg_colour)
        group_name_entry.grid(row=entry_id+2, column=1, columnspan=1, pady=15)
        self.group_name_entries.append(group_name_entry)

    def _draw_group_name_button(self, button_id):
        group_name_button_style = ttk.Style()
        group_name_button_style.theme_use('default')
        group_name_button_style.configure('Group.TButton', padding=6, relief="flat", font=(
            'Georgia', 12, 'bold'), background='#cc2b5b', foreground='black')
        group_name_button_style.map('Group.TButton', background=[('active', '#fa2039'), (
            'disabled', '#ba2d3d')], foreground=[('pressed', '#361317'), ('active', 'black')])
        group_name_button = ttk.Button(master=self, text="Rename group", style='Group.TButton',
                                   command=lambda:self.handle_group_name_button(button_id))
        group_name_button.grid(row=button_id+2, column=2, columnspan=1, pady=15)



        
    def handle_group_name_button(self, button_id):
        print("handle_group_name_button: button_id = ", button_id)
        entry_value = self.group_name_entries[button_id].get()
        print("handle_group_name_button: entry_value = ", entry_value)

