from tkinter import ttk, Toplevel, StringVar, constants, scrolledtext, Canvas, LEFT, BOTH, RIGHT, Y, VERTICAL
from .styles import configure_management_window_styles, bg_colour


class ManagementWindow(Toplevel):
    """A class representing the management window that contains tools for adding, modifying and deleting message templates."""

    def __init__(self, master=None, message_handler=None, update_combobox_groups_func=None, update_combobox_contents_func=None):
        """Constructor for ManagementWindow.

        Args:
            master: The parent of the management window, in this case the main window of the program.
            message_handler: An object that connucates with the database query classes, and modifies the fetched data into suitable form for ui.
            update_combobox_groups_func: A function to update the groups of the main window comboboxes.
            update_combobox_contents_func: A function to update the contents of the main window comboboxes.
            """

        super().__init__(master)

        self._root = master
        self._message_handler = message_handler
        self.update_combobox_groups_func = update_combobox_groups_func
        self.update_combobox_contents_func = update_combobox_contents_func

        self.title("Manage Message Templates")

    def start(self):
        """Start the management window

        This method initializes and displays the management window by creating a canvas and setting up scrollbar for the window.
        It retrieves the group names and message texts from
        the message handler and calls the drawing functiions for the UI elements such as text fields and buttons.
        """

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
        self.protocol("WM_DELETE_WINDOW", self._on_close)

        self.group_names = self._message_handler.group_name_list()
        self.messages = self._message_handler.all_messages_grouped()

        self.main_frame.grid_rowconfigure(
            (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17), weight=0)
        self.main_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)

        self._draw_header1()
        self._draw_header2()

        self._draw_message_template_area()

    def _on_mousewheel(self, event):
        """
        Handle mousewheel event.

        This method is called when a mousewheel event occurs. 
        It adjusts the scrolling of the canvas based on the mousewheel event value.

        Args:
            event (Event): The mousewheel event object.
        """
        if hasattr(self, "canvas"):
            self.canvas.yview_scroll(-1 * (event.delta // 120), "units")

    def _on_content_resize(self, event):
        """
        Handle content resize event.

        This method is called when the management window is resized. 
        It adjusts the scroll region to match the new size.

        Args:
            event (Event): The content resize event object.
        """
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def _on_close(self):
        """
        Handle window close event.

        This method is called when the management window is closed. 
        It unbinds the mousewheel and resize events from the management window
        components. If this was not done, it would cause an exeption, if the mousewheel
        would be used after closing the management window.
        To be safe, it also destroys the canvas, scrollbar and the whole management window.
        """
        self.canvas.unbind_all("<MouseWheel>")
        self.main_frame.unbind("<Configure>")
        self.canvas.destroy()
        self.scrollbar.destroy()
        self.destroy()

    def _draw_message_template_area(self):
        """
        Draw the message template area.

        This method creates the message template area of the management window. 
        For every message group it calls the drawing functions for:
            - group name header
            - input field and button for changing the group name
            - new template adding button
            - message modification controls for every message template
        """
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

    def _draw_header1(self):
        """
        Draw the main header of the management window.

        This method creates the first and biggest header containing the 
        program name "Boring Email Generator".
        """
        header1_label = ttk.Label(
            master=self.main_frame, text="Boring Email Generator")
        header1_label.config(font=("Georgia", 30, "bold"),
                             background=bg_colour)
        header1_label.grid(row=0, column=0, columnspan=4, pady=15)

    def _draw_header2(self):
        """
        Draw the second header of the management window.

        This method creates the second header containing the window name 
        and instruction "Modify templates".
        """
        header2_label = ttk.Label(
            master=self.main_frame, text="Modify templates")
        header2_label.config(font=("Georgia", 20, "bold"),
                             background=bg_colour)
        header2_label.grid(row=1, column=0, columnspan=1,
                           padx=15, pady=15, sticky="w")

    def _draw_header3(self, header3_id, group_name_variable):
        """
        Draw the group header in the message template area.

        This method creates the header for a group, containing the name 
        of the group in question.

        Args:
            header3_id (Event): The content resize event object.
            group_name_variable (StringVar)
        """
        header3_label = ttk.Label(
            master=self.main_frame, textvariable=group_name_variable)
        header3_label.config(font=("Georgia", 15, "bold"),
                             background=bg_colour)
        header3_label.grid(row=2*header3_id+2, column=0,
                           columnspan=1, padx=15, pady=(40, 5), sticky="w")
        self.group_name_headers.append(header3_label)

    def _draw_group_name_entry(self, entry_id):
        """
        Draw the group name entry in the message template area.

        This method creates an input field for changing the group name of 
        the group in question.
        """
        group_name_entry = ttk.Entry(master=self.main_frame)
        group_name_entry.grid(row=2*entry_id+2, column=1,
                              columnspan=1, padx=15, pady=(40, 5), sticky="we")
        self.group_name_entries.append(group_name_entry)

    def _draw_group_name_button(self, button_id):
        """
        Draw the group name button in the message template area.

        This method creates a button for changing the group name of 
        the group in question.
        """
        group_name_button = ttk.Button(master=self.main_frame, text="Rename group", style='Group.TButton',
                                       command=lambda: self.handle_group_name_button(button_id))
        group_name_button.grid(row=2*button_id+2, column=2, columnspan=1,
                               padx=15, pady=(40, 5), sticky=(constants.E, constants.W))
        self.group_name_buttons.append(group_name_button)

    def _draw_new_message_button(self, button_id):
        """
        Draw the new message button in the message template area.

        This method creates a button for changing the new message of 
        the group in question.
        """

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
        entry_value = self.group_name_entries[button_id].get()
        self._message_handler.rename_group(button_id, entry_value)
        self.group_name_variables[button_id].set(
            f"Group #{button_id+1}: {entry_value}")
        self.update_combobox_groups_func()


# DELETE OR MODIFY EXISTING MESSAGE TEMPLATES:


    def handle_delete_message_button(self, frame_id, button_id):
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
        self._message_handler.update_message(
            self.messages[frame_id][message_id], text)
        self.messages = self._message_handler.all_messages_grouped()

        self.group_message_frames[frame_id].destroy()
        self.group_message_frames[frame_id] = self._draw_group_frame(frame_id)

        self._draw_message_controls(frame_id)
        self.update_combobox_contents_func()


# CREATE A NEW MESSAGE TEMPLATE:


    def handle_new_message_button(self, button_id):
        place = len(self.messages[button_id])
        text = "Type your new message template here!"
        new_text_entry = self.draw_message_text_area(button_id, place, text)
        self._draw_group_placeholder_label(button_id, place)
        self._draw_cancel_message_button(button_id, place)
        self._draw_create_message_button(button_id, place)
        self.create_message_entries[button_id] = new_text_entry

    def handle_cancel_message_button(self, frame_id):
        self.group_message_frames[frame_id].destroy()
        self.group_message_frames[frame_id] = self._draw_group_frame(frame_id)
        self._draw_message_controls(frame_id)
        self.create_message_entries[frame_id] = None

    def handle_create_message_button(self, frame_id):
        text = self.create_message_entries[frame_id].get('1.0', 'end-1c')
        group = frame_id
        self._message_handler.add_new_message(group, text)
        self.messages = self._message_handler.all_messages_grouped()

        self.group_message_frames[frame_id].destroy()
        self.group_message_frames[frame_id] = self._draw_group_frame(frame_id)

        self._draw_message_controls(frame_id)
        self.update_combobox_contents_func()
