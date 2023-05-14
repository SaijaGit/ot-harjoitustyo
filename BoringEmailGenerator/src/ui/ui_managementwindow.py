from tkinter import ttk, Toplevel, StringVar, constants, scrolledtext, Canvas, LEFT, BOTH, RIGHT, Y, VERTICAL
from .styles import configure_management_window_styles, bg_color 


class ManagementWindow(Toplevel):
    """
    A class representing the management window that contains tools for adding, modifying and 
    deleting message templates.
    """

    def __init__(self, master, message_handler, update_combobox_groups_func, update_combobox_contents_func):
        """Constructor for ManagementWindow.

        Args:
            master (MainWindow): The parent of the management window, in this case the main window of the program.
            message_handler (MessageHandler): Helper class that passes the requests to the database
            query class, and modifies the fetched data into suitable form for ui.
            update_combobox_groups_func: A function to update the groups of the main window comboboxes.
            update_combobox_contents_func: A function to update the contents of the main window comboboxes.
            """

        super().__init__(master)

        self._root = master
        self._message_handler = message_handler
        self._update_combobox_groups_func = update_combobox_groups_func
        self._update_combobox_contents_func = update_combobox_contents_func

        self.title("Manage Message Templates")

    def start(self):
        """Start the management window

        This method initializes and displays the management window by creating a canvas and 
        setting up scrollbar for the window.
        It retrieves the message texts from the message handler and starts the drawing of all 
        the window content.
        """

        configure_management_window_styles()

        self._group_message_frames = []
        self._group_name_variables = []
        self._group_name_entries = []
        self._group_name_headers = []
        self._group_name_buttons = []
        self._modify_message_entries = []
        self._new_message_buttons = []
        self._create_message_entries = {}

        self.minsize(860, 0)

        self._canvas = Canvas(self, width=800, height=800)
        self._canvas.pack(side=LEFT, fill=BOTH, expand=True)

        self._main_frame = ttk.Frame(self._canvas, style='Group.TFrame')
        self._canvas.create_window((0, 0), window=self._main_frame, anchor="nw")

        self._scrollbar = ttk.Scrollbar(
            self, orient=VERTICAL, command=self._canvas.yview)
        self._scrollbar.pack(side=RIGHT, fill=Y)
        self._canvas.configure(yscrollcommand=self._scrollbar.set)

        self._canvas.bind_all("<MouseWheel>", self._on_mousewheel)
        self._main_frame.bind("<Configure>", self._on_content_resize)

        self.configure(bg=bg_color)
        self._canvas.configure(bg=bg_color)
        self.protocol("WM_DELETE_WINDOW", self._on_close)

        self._messages = self._message_handler.all_messages_grouped()

        self._main_frame.grid_rowconfigure(
            (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17), weight=0)
        self._main_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)

        self._draw_header1()
        self._draw_header2()

        self._draw_message_template_area()


    def _on_mousewheel(self, event):
        """Handle mousewheel event.

        This method is called when a mousewheel event occurs. 
        It adjusts the scrolling of the canvas based on the mousewheel event value.

        Args:
            event (Event): The mousewheel event object.
        """
        if hasattr(self, "_canvas"):
            self._canvas.yview_scroll(-1 * (event.delta // 120), "units")


    def _on_content_resize(self, event):
        """Handle content resize event.

        This method is called when the management window is resized. 
        It adjusts the scroll region to match the new size.

        Args:
            event (Event): The content resize event object.
        """
        self._canvas.configure(scrollregion=self._canvas.bbox("all"))


    def _on_close(self):
        """Handle window close event.

        This method is called when the management window is closed. 
        It unbinds the mousewheel and resize events from the management window
        components. If this was not done, it would cause an exeption, if the mousewheel
        would be used after closing the management window.
        To be safe, it also destroys the canvas, scrollbar and the whole management window.
        """
        self._canvas.unbind_all("<MouseWheel>")
        self._main_frame.unbind("<Configure>")
        self._canvas.destroy()
        self._scrollbar.destroy()
        self.destroy()


    def _draw_message_template_area(self):
        """Draw the message template area.

        This method creates the message template area of the management window. 
        For every message group it calls the drawing functions for:
            - group name header
            - input field and button for changing the group name
            - new template adding button
            - an inner frame for message templatess
            - message modification controls for every message template
        """
        group_names = self._message_handler.group_name_list()
        for i in range(8):
            group_name = f"Group #{i+1}: {group_names[i]}"
            self._group_name_variables.append(StringVar())
            self._group_name_variables[i].set(group_name)
            self._draw_header3((i), self._group_name_variables[i])
            self._draw_group_name_entry(i)
            self._draw_group_name_button(i)
            self._draw_new_message_button(i)
            self._group_message_frames.append(self._draw_group_message_frame(i))
            self._draw_message_controls(i)

    def _draw_header1(self):
        """Draw the main header of the management window.

        This method creates the first and biggest header containing the 
        program name "Boring Email Generator".
        """
        header1_label = ttk.Label(
            master=self._main_frame, text="Boring Email Generator")
        header1_label.config(font=("Georgia", 30, "bold"),
                             background=bg_color)
        header1_label.grid(row=0, column=0, columnspan=4, pady=15)


    def _draw_header2(self):
        """Draw the second header of the management window.

        This method creates the second header containing the window name 
        and instruction "Modify templates".
        """
        header2_label = ttk.Label(
            master=self._main_frame, text="Modify templates")
        header2_label.config(font=("Georgia", 20, "bold"),
                             background=bg_color)
        header2_label.grid(row=1, column=0, columnspan=1,
                           padx=15, pady=15, sticky="w")


    def _draw_header3(self, header3_id, group_name_variable):
        """Draw the group header in the message template area.

        This method creates the header for a group, containing the name 
        of the group in question.

        Args:
            header3_id (int): Index of the group in self._group_name_variables
            group_name_variable (StringVar): Group name as StringVar, because
            it is needed to be changeable
        """
        header3_label = ttk.Label(
            master=self._main_frame, textvariable=group_name_variable)
        header3_label.config(font=("Georgia", 15, "bold"),
                             background=bg_color)
        header3_label.grid(row=2*header3_id+2, column=0,
                           columnspan=1, padx=15, pady=(40, 5), sticky="w")
        self._group_name_headers.append(header3_label)


    def _draw_group_name_entry(self, entry_id):
        """Draw the group name entry in the message template area.

        This method creates an input field for changing the group name of 
        the group in question.

        Args:
            entry_id (int): Index of the group (0...7)
        """
        group_name_entry = ttk.Entry(master=self._main_frame)
        group_name_entry.grid(row=2*entry_id+2, column=1,
                              columnspan=1, padx=15, pady=(40, 5), sticky="we")
        self._group_name_entries.append(group_name_entry)


    def _draw_group_name_button(self, button_id):
        """Draw the group name button in the message template area.

        This method creates a button for changing the group name of 
        the group in question.

        Args:
            button_id (int): Index of the group (0...7)
        """
        group_name_button = ttk.Button(master=self._main_frame, text="Rename group", style='Group.TButton',
                                       command=lambda: self._handle_group_name_button(button_id))
        group_name_button.grid(row=2*button_id+2, column=2, columnspan=1,
                               padx=15, pady=(40, 5), sticky=(constants.E, constants.W))
        self._group_name_buttons.append(group_name_button)


    def _draw_new_message_button(self, button_id):
        """Draw the new message button in the message template area.

        This method creates a button for changing the new message of 
        the group in question.
        
        Args:
            button_id (int): Index of the group (0...7)
        """
        new_message__button = ttk.Button(master=self._main_frame, text="Add new template", style='New.TButton',
                                         command=lambda: self._handle_new_message_button(button_id))
        new_message__button.grid(row=2*button_id+2, column=3, columnspan=1,
                                 padx=15, pady=(40, 5), sticky=(constants.E, constants.W))
        self._new_message_buttons.append(new_message__button)


    def _draw_group_message_frame(self, frame_id):
        """Creates a separate inner frame for displaying messages.

        Each group needs its own frame for displaying the message templates and all their
        widgets because the number of the messages in each group varies and changes, and 
        therefore they are difficult to handle in the main frame of the window.
        
        Args:
            frame_id (int): Index of the group (0...7)

        Returns:
            group_frame (Frame): Meassge frame of the group.
        """
        group_frame = ttk.Frame(self._main_frame, style='Group.TFrame')
        group_frame.grid(row=frame_id*2+3, column=0,
                         columnspan=4, padx=5, pady=10, sticky="ne")
        group_frame.grid_columnconfigure((2, 3), weight=0)
        group_frame.grid_columnconfigure((0, 1), weight=1)
        return group_frame


    def _draw_message_controls(self, frame_id):
        """Fills the message frame with the message widgets.

        Calls for the drawing fucntions for all the message buttons and text for all messages of a group.
        
        Args:
            frame_id (int): Index of the group (0...7)
        """
        message_count = len(self._messages[frame_id])
        for i in range(message_count):
            text_area = self._draw_message_text_area(
                frame_id, i, self._messages[frame_id][i].text)
            self._draw_group_placeholder_label(frame_id, i)
            self._draw_delete_message_button(frame_id, i)
            self._draw_save_message_button(frame_id, i, text_area)

        
        """Adds a scrollable text area for showing the message text.
        
        Args:
            frame_id (int): Index of the group (0...7)
            message_id (int): Index of the message in the group
            message_text (str): Message text to show
        """
    def _draw_message_text_area(self, frame_id, message_id, message_text):
        message_entry = scrolledtext.ScrolledText(
            master=self._group_message_frames[frame_id], height=6, wrap="word")
        message_entry.insert('end', message_text)
        message_entry.grid(row=message_id*2, column=0, columnspan=4, sticky=(
            constants.E, constants.W), padx=2, pady=(15, 2))
        return message_entry
    
    
    def _draw_group_placeholder_label(self, frame_id, message_id):
        """Just a placeholder to keep the grid pretty.

        Adds an empty label next of the buttons of a message to keep the button width right.
        
        Args:
            frame_id (int): Index of the group (0...7)
            message_id (int): Index of the message in the group
        """
        placeholder_label = ttk.Label(
            master=self._group_message_frames[frame_id], text="", style='Group.TFrame')
        placeholder_label.grid(row=message_id*2+1, column=0, columnspan=2, sticky=(
            constants.E, constants.W), padx=2, pady=2)

    def _draw_delete_message_button(self, frame_id, message_id):
        """Adds a button for deleting the message template.
        
        Args:
            frame_id (int): Index of the group (0...7)
            message_id (int): Index of the message in the group
        """
        delete_message_button = ttk.Button(master=self._group_message_frames[frame_id], text=f"Delete", style='Delete.TButton',
                                           command=lambda: self._handle_delete_message_button(frame_id, message_id))
        delete_message_button.grid(
            row=message_id*2+1, column=2, columnspan=1, padx=5, pady=5, sticky=(constants.E, constants.W))


    def _draw_save_message_button(self, frame_id, message_id, text_area):
        """Adds a button for saving the changes for message template.
        
        Args:
            frame_id (int): Index of the group (0...7)
            message_id (int): Index of the message in the group
            text_area (ScrolledText): Text area where the new message text is taken from
        """
        save_message_button = ttk.Button(master=self._group_message_frames[frame_id], text=f"Save", style='Save.TButton',
                                         command=lambda: self._handle_save_message_button(frame_id, message_id, text_area))
        save_message_button.grid(row=message_id*2+1, column=3, columnspan=1,
                                 padx=5, pady=5, sticky=(constants.E, constants.W))


    def _draw_cancel_message_button(self, frame_id, message_id):
        """Adds a button that cancels the creation of a new message template.

        This button is added into group's message frame after the "new message button" is clicked.
        
        Args:
            frame_id (int): Index of the group (0...7)
            message_id (int): Index for the new message, one bigger than the previous last message of this group
        
        Returns:
            cancel_message_button (Button): New cancel button
        """
        cancel_message_button = ttk.Button(master=self._group_message_frames[frame_id], text=f"Cancel", style='Cancel.TButton',
                                           command=lambda: self._handle_cancel_message_button(frame_id))
        cancel_message_button.grid(
            row=message_id*2+1, column=2, columnspan=1, padx=5, pady=5, sticky=(constants.E, constants.W))
        return cancel_message_button


    def _draw_create_message_button(self, frame_id, message_id):
        """Adds a button that creates a new message template.

        This button is added into group's message frame after the "new message button" is clicked.
        
        Args:
            frame_id (int): Index of the group (0...7)
            message_id (int): Index for the new message, one bigger than the previous last message of this group
        
        Returns:
            create_message_button (Button): New create button
        """
        create_message_button = ttk.Button(master=self._group_message_frames[frame_id], text=f"Create", style='Create.TButton',
                                           command=lambda: self._handle_create_message_button(frame_id))
        create_message_button.grid(
            row=message_id*2+1, column=3, columnspan=1, padx=5, pady=5, sticky=(constants.E, constants.W))
        return create_message_button


# BUTTONS:
# CHANGE GROUP NAME:

    def _handle_group_name_button(self, button_id):
        """Handler for group name change button

        Requests MessageHandler for the change and updates both of the windows with the new group name.
        
        Args:
            button_id (int): Index of the group (0...7)
        """
        entry_value = self._group_name_entries[button_id].get()
        self._message_handler.rename_group(button_id, entry_value)
        self._group_name_variables[button_id].set(
            f"Group #{button_id+1}: {entry_value}")
        self._update_combobox_groups_func()


# DELETE OR MODIFY EXISTING MESSAGE TEMPLATES:


    def _handle_delete_message_button(self, frame_id, button_id):
        """Handler for message delete button

        Requests MessageHandler for the message deletion and removes deleted message from both of the windows.
        
        Args:
            frame_id (int): Index of the group (0...7)
            button_id (int): Index of the message in the group
        """
        self._message_handler.delete_message(
            self._messages[frame_id][button_id])
        self._messages = self._message_handler.all_messages_grouped()

        self._group_message_frames[frame_id].destroy()
        self._group_message_frames[frame_id] = self._draw_group_message_frame(frame_id)

        self._draw_message_controls(frame_id)
        self._update_combobox_contents_func()


    def _handle_save_message_button(self, frame_id, message_id, text_area):
        """Handler for message save button

        Requests MessageHandler for the message update and updates the message text to both of the windows.
        
        Args:
            frame_id (int): Index of the group (0...7)
            button_id (int): Index of the message in the group
            text_area (ScrolledText): Text area containing the updated message text
        """
        text = text_area.get('1.0', 'end-1c')

        self._message_handler.update_message(
            self._messages[frame_id][message_id], text)
        self._messages = self._message_handler.all_messages_grouped()

        self._group_message_frames[frame_id].destroy()
        self._group_message_frames[frame_id] = self._draw_group_message_frame(frame_id)

        self._draw_message_controls(frame_id)
        self._update_combobox_contents_func()


# CREATE A NEW MESSAGE TEMPLATE:


    def _handle_new_message_button(self, button_id):
        """Handler for new message button

        Draws the text area and buttons needed to add a new message template into the group.
        
        Args:
            button_id (int): Index of the group (0...7)
        """
        place = len(self._messages[button_id])
        text = "Type your new message template here!"
        new_text_entry = self._draw_message_text_area(button_id, place, text)
        self._draw_group_placeholder_label(button_id, place)
        self._draw_cancel_message_button(button_id, place)
        self._draw_create_message_button(button_id, place)
        self._create_message_entries[button_id] = new_text_entry


    def _handle_cancel_message_button(self, frame_id):
        """Handler for cancel the new message creation button

        Removes the new message creation text area and buttons from the window.
        
        Args:
            frame_id (int): Index of the group (0...7) in which the message was to be added
        """
        self._group_message_frames[frame_id].destroy()
        self._group_message_frames[frame_id] = self._draw_group_message_frame(frame_id)
        self._draw_message_controls(frame_id)
        self._create_message_entries[frame_id] = None


    def _handle_create_message_button(self, frame_id):
        """Handler for create new message button

        Asks the MessageHandler to add the new message and adds it also into both of the ui windows.
        
        Args:
            frame_id (int): Index of the group (0...7) of the new message
        """
        text = self._create_message_entries[frame_id].get('1.0', 'end-1c')
        group = frame_id
        self._message_handler.add_new_message(group, text)
        self._messages = self._message_handler.all_messages_grouped()

        self._group_message_frames[frame_id].destroy()
        self._group_message_frames[frame_id] = self._draw_group_message_frame(frame_id)

        self._draw_message_controls(frame_id)
        self._update_combobox_contents_func()
