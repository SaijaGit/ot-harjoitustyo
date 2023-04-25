from tkinter import ttk, Toplevel, StringVar, constants, scrolledtext, Canvas, LEFT, BOTH, RIGHT, Y, VERTICAL
from .styles import configure_management_window_styles, bg_colour


class ManagementWindow(Toplevel):
    def __init__(self, master=None, message_handler=None, update_combobox_groups_func=None, update_combobox_contents_func=None):
        super().__init__(master)

        self._root = master
        self._message_handler = message_handler
        self.update_combobox_groups_func = update_combobox_groups_func
        self.update_combobox_contents_func = update_combobox_contents_func

        self.title("Manage Message Templates")

    def start(self):

        configure_management_window_styles()

        self.group_message_frames = []
        self.group_name_variables = []
        self.group_name_entries = []
        self.group_name_headers = []
        self.group_name_buttons = []
        self.modify_message_entries = []
        self.new_message_buttons = []
        self.create_message_entries = {}

        self.minsize(840, 0)

        self.canvas = Canvas(self, width=800, height=800)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)

        self.main_frame = ttk.Frame(self.canvas, style='Group.TFrame')
        self.canvas.create_window((0, 0), window=self.main_frame, anchor="nw")

        self.scrollbar = ttk.Scrollbar(
            self, orient=VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)
        self.main_frame.bind("<Configure>", self._on_content_resize)

        self.configure(bg=bg_colour)
        self.canvas.configure(bg=bg_colour)

        self.group_names = self._message_handler.group_name_list()
        self.messages = self._message_handler.all_messages_grouped()

        self.main_frame.grid_rowconfigure(
            (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17), weight=0)
        self.main_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)

        self._draw_header1()
        self._draw_header2()

        self._draw_message_template_area()

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(-1 * (event.delta // 120), "units")

    def _on_content_resize(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def _draw_message_template_area(self):
        for i in range(8):
            group_name = f"Group #{i+1}: {self.group_names[i]}"
            self.group_name_variables.append(StringVar())
            self.group_name_variables[i].set(group_name)
            self._draw_header3((i), self.group_name_variables[i])
            self._draw_group_name_entry(i)
            self._draw_group_name_button(i)
            self._draw_new_message_button(i)
            self.group_message_frames.append(self._draw_group_frame(i))
            self._draw_message_controls(i)

        # self.main_frame.pack(fill=BOTH, expand=True)

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
        header2_label.grid(row=1, column=0, columnspan=1,
                           padx=15, pady=15, sticky="w")

    def _draw_header3(self, header3_id, group_name_variable):
        header3_label = ttk.Label(
            master=self.main_frame, textvariable=group_name_variable)
        header3_label.config(font=("Georgia", 15, "bold"),
                             background=bg_colour)
        header3_label.grid(row=2*header3_id+2, column=0,
                           columnspan=1, padx=15, pady=(40, 5), sticky="w")
        self.group_name_headers.append(header3_label)

    def _draw_group_name_entry(self, entry_id):
        group_name_entry = ttk.Entry(master=self.main_frame)
        group_name_entry.grid(row=2*entry_id+2, column=1,
                              columnspan=1, padx=15, pady=(40, 5), sticky="we")
        self.group_name_entries.append(group_name_entry)

    def _draw_group_name_button(self, button_id):
        group_name_button = ttk.Button(master=self.main_frame, text="Rename group", style='Group.TButton',
                                       command=lambda: self.handle_group_name_button(button_id))
        group_name_button.grid(row=2*button_id+2, column=2, columnspan=1,
                               padx=15, pady=(40, 5), sticky=(constants.E, constants.W))
        self.group_name_buttons.append(group_name_button)

    def _draw_new_message_button(self, button_id):
        new_message__button = ttk.Button(master=self.main_frame, text="Add new template", style='New.TButton',
                                         command=lambda: self.handle_new_message_button(button_id))
        new_message__button.grid(row=2*button_id+2, column=3, columnspan=1,
                                 padx=15, pady=(40, 5), sticky=(constants.E, constants.W))
        self.new_message_buttons.append(new_message__button)

    def _draw_group_frame(self, frame_id):
        group_frame = ttk.Frame(self.main_frame, style='Group.TFrame')
        group_frame.grid(row=frame_id*2+3, column=0,
                         columnspan=4, padx=5, pady=10, sticky="ne")
        group_frame.grid_columnconfigure((2, 3), weight=0)
        group_frame.grid_columnconfigure((0, 1), weight=1)
        return group_frame
        # self.group_message_frames.append(group_frame)

    def _draw_message_controls(self, frame_id):
        message_count = len(self.messages[frame_id])
        for i in range(message_count):
            text_area = self.draw_message_text_area(
                frame_id, i, self.messages[frame_id][i].text)
            self._draw_group_placeholder_label(frame_id, i)
            self._draw_delete_message_button(frame_id, i)
            self._draw_save_message_button(frame_id, i, text_area)

    def draw_message_text_area(self, frame_id, message_id, message_text):
        message_entry = scrolledtext.ScrolledText(
            master=self.group_message_frames[frame_id], height=6, wrap="word")
        message_entry.insert('end', message_text)
        message_entry.insert(
            'end', f"Frame id: {frame_id}, message_id: {message_id}, row = {message_id*2}")
        message_entry.grid(row=message_id*2, column=0, columnspan=4, sticky=(
            constants.E, constants.W), padx=2, pady=(15, 2))
        return message_entry

    def _draw_group_placeholder_label(self, frame_id, message_id):
        placeholder_label = ttk.Label(
            master=self.group_message_frames[frame_id], text="", style='Group.TFrame')
        placeholder_label.grid(row=message_id*2+1, column=0, columnspan=2, sticky=(
            constants.E, constants.W), padx=2, pady=2)

    def _draw_delete_message_button(self, frame_id, message_id):
        delete_message_button = ttk.Button(master=self.group_message_frames[frame_id], text=f"Delete", style='Delete.TButton',
                                           command=lambda: self.handle_delete_message_button(frame_id, message_id))
        delete_message_button.grid(
            row=message_id*2+1, column=2, columnspan=1, padx=5, pady=5, sticky=(constants.E, constants.W))

    def _draw_save_message_button(self, frame_id, message_id, text_area):
        save_message_button = ttk.Button(master=self.group_message_frames[frame_id], text=f"Save", style='Save.TButton',
                                         command=lambda: self.handle_save_message_button(frame_id, message_id, text_area))
        save_message_button.grid(row=message_id*2+1, column=3, columnspan=1,
                                 padx=5, pady=5, sticky=(constants.E, constants.W))

    def _draw_cancel_message_button(self, frame_id, message_id):
        cancel_message_button = ttk.Button(master=self.group_message_frames[frame_id], text=f"Cancel", style='Cancel.TButton',
                                           command=lambda: self.handle_cancel_message_button(frame_id))
        cancel_message_button.grid(
            row=message_id*2+1, column=2, columnspan=1, padx=5, pady=5, sticky=(constants.E, constants.W))
        return cancel_message_button

    def _draw_create_message_button(self, frame_id, message_id):
        create_message_button = ttk.Button(master=self.group_message_frames[frame_id], text=f"Create", style='Create.TButton',
                                           command=lambda: self.handle_create_message_button(frame_id))
        create_message_button.grid(
            row=message_id*2+1, column=3, columnspan=1, padx=5, pady=5, sticky=(constants.E, constants.W))
        return create_message_button


# BUTTONS:
# CHANGE GROUP NAME:


    def handle_group_name_button(self, button_id):
        print("handle_group_name_button: button_id = ", button_id)
        entry_value = self.group_name_entries[button_id].get()
        print("handle_group_name_button: entry_value = ", entry_value)
        self._message_handler.rename_group(button_id, entry_value)
        self.group_name_variables[button_id].set(
            f"Group #{button_id+1}: {entry_value}")
        self.update_combobox_groups_func()


# DELETE OR MODIFY EXISTING MESSAGE TEMPLATES:


    def handle_delete_message_button(self, frame_id, button_id):
        print("handle_delete_message_button: frame_id = ",
              frame_id, ", button_id = ", button_id)
        print(
            "handle_delete_message_button: self.group_message_frames[frame_id][button_id] = ", self.group_message_frames[frame_id])
        self._message_handler.delete_message(
            self.messages[frame_id][button_id])
        self.messages = self._message_handler.all_messages_grouped()

        self.group_message_frames[frame_id].destroy()
        self.group_message_frames[frame_id] = self._draw_group_frame(frame_id)

        self._draw_message_controls(frame_id)
        self.update_combobox_contents_func()

    def handle_save_message_button(self, frame_id, message_id, text_area):
        text = text_area.get('1.0', 'end-1c')
        group = frame_id
        print("handle_save_message_button: group = ", group, ", text = ", text)
        self._message_handler.update_message(
            self.messages[frame_id][message_id], text)
        self.messages = self._message_handler.all_messages_grouped()

        self.group_message_frames[frame_id].destroy()
        self.group_message_frames[frame_id] = self._draw_group_frame(frame_id)

        self._draw_message_controls(frame_id)
        self.update_combobox_contents_func()


# CREATE A NEW MESSAGE TEMPLATE:


    def handle_new_message_button(self, button_id):
        print("handle_new_message_button: button_id = ", button_id)
        place = len(self.messages[button_id])
        text = "Type your new message template here!"
        new_text_entry = self.draw_message_text_area(button_id, place, text)
        self._draw_group_placeholder_label(button_id, place)
        self._draw_cancel_message_button(button_id, place)
        self._draw_create_message_button(button_id, place)
        self.create_message_entries[button_id] = new_text_entry
        # self.messages[button_id].append(text)
        # self.draw_message_text_area(button_id, len(self.messages[button_id]), "Type your new message template here!")

    def handle_cancel_message_button(self, frame_id):
        print("handle_cancel_message_button: button_id = ", frame_id)
        self.group_message_frames[frame_id].destroy()
        self.group_message_frames[frame_id] = self._draw_group_frame(frame_id)
        self._draw_message_controls(frame_id)
        self.create_message_entries[frame_id] = None

    def handle_create_message_button(self, frame_id):
        text = self.create_message_entries[frame_id].get('1.0', 'end-1c')
        group = frame_id
        print("handle_create_message_button: group = ", group, ", text = ", text)
        self._message_handler.add_new_message(group, text)
        self.messages = self._message_handler.all_messages_grouped()

        self.group_message_frames[frame_id].destroy()
        self.group_message_frames[frame_id] = self._draw_group_frame(frame_id)

        self._draw_message_controls(frame_id)
        self.update_combobox_contents_func()
