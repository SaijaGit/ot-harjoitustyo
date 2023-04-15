from tkinter import Tk, ttk, Toplevel, StringVar, constants, scrolledtext, Canvas, LEFT, BOTH, RIGHT, Y, VERTICAL


bg_colour = "#bbe1fa"

class ManagementWindow(Toplevel):
    def __init__(self, master=None, message_handler=None, update_combobox_groups_func=None, update_combobox_contents_func=None):
        super().__init__(master)

        self._root = master
        self._message_handler = message_handler
        self.update_combobox_groups_func = update_combobox_groups_func
        self.update_combobox_contents_func = update_combobox_contents_func

        self.title("Manage Message Templates")


    def start(self):

        self.group_name_variables = []
        self.group_name_entries = []
        self.group_name_headers = []
        self.group_name_buttons = []
        self.new_message_buttons = []
        self.group_message_frames = []
        self.group_controls = []


        self.canvas=Canvas(self, width=800, height=600)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)
        main_frame_style = ttk.Style()
        main_frame_style.configure('My.TFrame', background=bg_colour)
        self.main_frame = ttk.Frame(self.canvas, style='My.TFrame')
        self.canvas.create_window((0,0), window=self.main_frame, anchor="nw")

        self.scrollbar = ttk.Scrollbar(self, orient=VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)
        self.main_frame.bind("<Configure>", self._on_content_resize)

        self.configure(bg=bg_colour)
        self.canvas.configure(bg=bg_colour)

        self.group_names = self._message_handler.group_name_list()
        self.messages = self._message_handler.all_messages_grouped()

        self.main_frame.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17), weight=0)
        self.main_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)
        
        self._draw_header1()
        self._draw_header2()

        self._draw_message_template_area()


    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(-1 * (event.delta // 120), "units")
        
    def _on_content_resize(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))


    def _draw_message_template_area(self):
        for i in range(8) :
            group_name=f"Group #{i+1}: {self.group_names[i]}"
            self.group_name_variables.append(StringVar())
            self.group_name_variables[i].set(group_name)
            self._draw_header3((i), self.group_name_variables[i])
            self._draw_group_name_entry(i)
            self._draw_group_name_button(i)
            self._draw_new_message_button(i)
            self._draw_group_frame(i)
            self._draw_message_controls(i)

        #self.main_frame.pack(fill=BOTH, expand=True)

    def _draw_header1(self):
        header1_label = ttk.Label(
            master=self.main_frame, text="Boring Email Generator")
        header1_label.config(font=("Georgia", 30, "bold"),
                             background=bg_colour)
        header1_label.grid(row=0, column=0, columnspan=4, pady=15)

    def _draw_header2(self):
        header2_label = ttk.Label(
            master=self.main_frame, text="Modify templates")
        header2_label.config(font=("Georgia", 20, "bold"),
                             background=bg_colour)
        header2_label.grid(row=1, column=0, columnspan=1, padx=15, pady=15, sticky="w")

    def _draw_header3(self, header3_id, group_name_variable):
        header3_label = ttk.Label(
            master=self.main_frame, textvariable=group_name_variable)
        header3_label.config(font=("Georgia", 15, "bold"),
                             background=bg_colour)
        header3_label.grid(row=2*header3_id+2, column=0, columnspan=1, padx=15, pady=15, sticky="w")
        self.group_name_headers.append(header3_label)

    def _draw_group_name_entry(self, entry_id):
        group_name_entry = ttk.Entry(master=self.main_frame)
        group_name_entry.grid(row=2*entry_id+2, column=1, columnspan=1, padx=15, pady=15, sticky="we")
        self.group_name_entries.append(group_name_entry)

    def _draw_group_name_button(self, button_id):
        group_name_button_style = ttk.Style()
        group_name_button_style.theme_use('default')
        group_name_button_style.configure('Group.TButton', padding=6, relief="flat", font=(
            'Georgia', 12, 'bold'), background='#d966ff', foreground='black')
        group_name_button_style.map('Group.TButton', background=[('active', '#ff66ff'), (
            'disabled', '#8c66ff')], foreground=[('pressed', '#660066'), ('active', 'black')])
        group_name_button = ttk.Button(master=self.main_frame, text="Rename group", style='Group.TButton',
                                   command=lambda:self.handle_group_name_button(button_id))
        group_name_button.grid(row=2*button_id+2, column=2, columnspan=1, padx=15, pady=15, sticky=(constants.E, constants.W))
        self.group_name_buttons.append(group_name_button)

    def _draw_new_message_button(self, button_id):
        group_new_message_style = ttk.Style()
        group_new_message_style.theme_use('default')
        group_new_message_style.configure('Group.TButton', padding=6, relief="flat", font=(
            'Georgia', 12, 'bold'), background='#d966ff', foreground='black')
        group_new_message_style.map('Group.TButton', background=[('active', '#ff66ff'), (
            'disabled', '#8c66ff')], foreground=[('pressed', '#660066'), ('active', 'black')])
        new_message__button = ttk.Button(master=self.main_frame, text="Add new template", style='Group.TButton',
                                   command=lambda:self.handle_new_message_button(button_id))
        new_message__button.grid(row=2*button_id+2, column=3, columnspan=1, padx=15, pady=15, sticky=(constants.E, constants.W))
        self.new_message_buttons.append(new_message__button)
    
    def _draw_group_frame(self, frame_id):
        group_frame = ttk.Frame(self.main_frame)
        group_frame.grid(row=frame_id*2+3, column=0, columnspan=4, padx=5, pady=10, sticky="ne")
        group_frame.grid_columnconfigure((2, 3), weight=0)
        group_frame.grid_columnconfigure((0, 1), weight=1)
        self.group_message_frames.append(group_frame)

    def _draw_message_controls(self, frame_id):
        message_count = len(self.messages[frame_id])
        for i in range(message_count):
            self.draw_message_text_area(frame_id, i, self.messages[frame_id][i].text)
            self._draw_group_placeholder_label(frame_id, i)
            self._draw_delete_message_button(frame_id, i)
            self._draw_save_message_button(frame_id, i)

    def draw_message_text_area(self, frame_id, message_id, message_text):
        message_entry = scrolledtext.ScrolledText(
            master=self.group_message_frames[frame_id], height=4, wrap="word")
        message_entry.insert('end', message_text)
        message_entry.insert('end', f"Frame id: {frame_id}, message_id: {message_id}, row = {message_id*2}")
        message_entry.grid(row=message_id*2, column=0, columnspan=4, sticky=(
            constants.E, constants.W), padx=2, pady=2)
        self.group_controls[frame_id].append(message_entry)
    
    def _draw_group_placeholder_label(self, frame_id, message_id):
            placeholder_label = ttk.Label(master=self.group_message_frames[frame_id], text="")
            placeholder_label.grid(row=message_id*2+1, column=0, columnspan=2, sticky=(
            constants.E, constants.W), padx=2, pady=2)
            self.group_controls[frame_id].append(placeholder_label)
    
    def _draw_delete_message_button(self, frame_id, message_id):
        delete_message_button_style = ttk.Style()
        delete_message_button_style.theme_use('default')
        delete_message_button_style.configure('Group.TButton', padding=2, relief="flat", font=(
            'Georgia', 12, 'bold'), background='#d966ff', foreground='black')
        delete_message_button_style.map('Group.TButton', background=[('active', '#ff66ff'), (
            'disabled', '#8c66ff')], foreground=[('pressed', '#660066'), ('active', 'black')])
        delete_message_button = ttk.Button(master=self.group_message_frames[frame_id], text=f"Delete", style='Group.TButton',
                                   command=lambda:self.handle_delete_message_button(frame_id, message_id))
        delete_message_button.grid(row=message_id*2+1, column=2, columnspan=1, padx=5, pady=5, sticky=(constants.E, constants.W))
        self.group_controls[frame_id].append(delete_message_button)
    
    def _draw_save_message_button(self, frame_id, message_id):
        save_message_button_style = ttk.Style()
        save_message_button_style.theme_use('default')
        save_message_button_style.configure('Group.TButton', padding=2, relief="flat", font=(
            'Georgia', 12, 'bold'), background='#d966ff', foreground='black')
        save_message_button_style.map('Group.TButton', background=[('active', '#ff66ff'), (
            'disabled', '#8c66ff')], foreground=[('pressed', '#660066'), ('active', 'black')])
        save_message_button = ttk.Button(master=self.group_message_frames[frame_id], text=f"Save", style='Group.TButton',
                                   command=lambda:self.handle_save_message_button(frame_id, message_id))
        save_message_button.grid(row=message_id*2+1, column=3, columnspan=1, padx=5, pady=5, sticky=(constants.E, constants.W))
        self.group_controls[frame_id].append(save_message_button)

        
    def handle_group_name_button(self, button_id):
        print("handle_group_name_button: button_id = ", button_id)
        entry_value = self.group_name_entries[button_id].get()
        print("handle_group_name_button: entry_value = ", entry_value)
        self._message_handler.rename_group(button_id, entry_value)
        self.group_name_variables[button_id].set(f"Group #{button_id+1}: {entry_value}")
        self.update_combobox_groups_func()

    def handle_new_message_button(self, button_id):
        print("handle_new_message_button: button_id = ", button_id)
        self.draw_message_text_area(button_id, len(self.messages[button_id]), "Type your new message template here!")

    def handle_delete_message_button(self, frame_id, button_id):
        print("handle_delete_message_button: frame_id = ", frame_id, ", button_id = ", button_id)
        print("handle_delete_message_button: self.group_message_frames[frame_id][button_id] = ", self.group_message_frames[frame_id])
        self._message_handler.delete_message(self.messages[frame_id][button_id])
        #self._update_main_frame()

        for item in self.group_controls[frame_id]:
            item.destroy()
        
        self.group_controls[frame_id] = [frame_id]
        self.messages = self._message_handler.all_messages_grouped()

        self._draw_message_controls()

        self.update_combobox_contents_func()
        

    def handle_save_message_button(self, frame_id, message_id):
        print("handle_save_message_button: frame_id = ", frame_id, ", message_id = ", message_id)
        
    def _update_main_frame(self):
        print("This should update the whole window")
        for group in range(8):
            self.group_name_entries[group].destroy()
            self.group_name_headers[group].destroy()
            self.group_name_buttons[group].destroy()
            self.new_message_buttons[group].destroy()
            self.group_message_frames[group].destroy()
        
        self.scrollbar.destroy()
        self.canvas.destroy()
        
        self.start()




