from tkinter import ttk, constants, scrolledtext
from .ui_managementwindow import ManagementWindow
from services.message_translator import MessageTranslator
from services.message_checker import MessageChecker
from .styles import configure_main_window_styles, bg_color


class MainWindow:
    """ A class representing the main window of the Boring Email Generator application.
    """

    def __init__(self, root, message_handler):
        """Constructor for MainWindow.

        Args:
            root (Tk): The tkinter root for the window.
            message_handler (MessageHandler): Helper class that passes the requests to the database
            query class, and modifies the fetched data into suitable form for ui.
            """
        self._root = root
        self._message_entry = None
        self._root.configure(bg=bg_color)

        self._message_handler = message_handler
        self._group_names = self._message_handler.group_name_list()
        self._message_texts = self._message_handler.all_message_texts_grouped()

        self._translator = MessageTranslator()
        self._checker = MessageChecker()
        self._translate_language_inputs = []

        self._management_window = None

        self._comboboxes = []


    def start(self):
        """Start the main window.

        Creates the window grid and fills in the content by calling their drawing methods.
        """
        configure_main_window_styles()

        self._root.grid_rowconfigure((0, 1, 2, 3, 4, 6), weight=0)
        self._root.grid_rowconfigure(5, weight=1)
        self._root.grid_columnconfigure((0, 1, 2, 3), weight=1)

        self._draw_header1()

        self._draw_comboboxes()

        self._draw_translate_inputs()

        self._draw_modify_content_button()

        self._draw_textarea()

        self._draw_text_area_buttons()


    def _draw_header1(self):
        """Draw the main header of the main window.

        This method creates the first and biggest header containing the 
        program name "Boring Email Generator".
        """
        header1_label = ttk.Label(
            master=self._root, text="Boring Email Generator")
        header1_label.config(font=("Georgia", 30, "bold"),
                             background=bg_color)
        header1_label.grid(row=0, column=0, columnspan=4, pady=15)


    def _draw_comboboxes(self):
        """Draws all the message template comboboxes into the main window.

        The comboboxes are placed on 2 rows and 4 columns.
        """
        for combobox_column in range(4):
            self._root.grid_columnconfigure(combobox_column, weight=1)

        for i in range(8):
            combobox = ttk.Combobox(
                master=self._root, values=self._message_texts[i], width=30, height=5, style='TCombobox')

            combobox.group_name = self._group_names[i]
            combobox.set(self._group_names[i])

            combobox.bind('<<ComboboxSelected>>', self._handle_comboboxes)

            if i < 4:
                row = 1
            else:
                row = 2
            column = i % 4

            combobox.grid(row=row, column=column, padx=10, pady=5, sticky="ew")
            self._comboboxes.append(combobox)
    

    def _draw_modify_content_button(self):
        """Draws button for opening the management window.
        """
        manage_button = ttk.Button(master=self._root, text="Modify templates",
                                   style='Manage.TButton', command=self._handle_management_window_button_click)
        manage_button.grid(row=3, column=3, columnspan=1,
                           padx=5, pady=10, sticky=(constants.E, constants.W))

    def _draw_textarea(self):
        """Draws a scrollable text area for messages.
        """
        self._message_entry = scrolledtext.ScrolledText(
            master=self._root, height=80, wrap="word")
        self._message_entry.grid(row=5, column=0, columnspan=4, sticky=(
            constants.E, constants.W), padx=15, pady=15)


    def _draw_text_area_buttons(self):
        """Draws 2 buttons under the text area.
        """
        delete_button = ttk.Button(master=self._root, text="Empty", style='Delete.TButton',
                                   command=lambda: self._message_entry.delete('1.0', 'end'))  # self._handle_delete_button_click)

        copy_button = ttk.Button(master=self._root, text="Copy",
                                 style='Copy.TButton', command=self._handle_copy_button_click)

        delete_button.grid(row=6, column=2, columnspan=1,
                           padx=10, pady=10, sticky=(constants.W, constants.E))
        copy_button.grid(row=6, column=3, columnspan=1,  padx=10,
                         pady=10, sticky=(constants.E, constants.W))


    def _draw_translate_inputs(self):
        """Draws the language selexting comboboxes and a button for translating.
        """
        language_list = self._translator.get_language_list()
        combobox_style = ttk.Style()
        combobox_style.configure('TCombobox', padding=(5, 2, 5, 2))

        language_from_combobox = ttk.Combobox(
            master=self._root, values=language_list, width=30, height=5, style='TCombobox')
        language_from_combobox.set("Translate from")

        language_to_combobox = ttk.Combobox(
            master=self._root, values=language_list, width=30, height=5, style='TCombobox')
        language_to_combobox.set("Translate to")

        language_from_combobox.grid(
            row=4, column=1, padx=10, pady=5, sticky="ew")
        language_to_combobox.grid(
            row=4, column=2, padx=10, pady=5, sticky="ew")
        self._translate_language_inputs = [
            language_from_combobox, language_to_combobox]

        translate_button = ttk.Button(master=self._root, text="Translate",
                                      style='Translate.TButton', command=self._handle_translate_button_click)

        translate_button.grid(row=4, column=3, columnspan=1,
                              padx=10, pady=10, sticky=(constants.W, constants.E))
        

    def _draw_translation_label(self):
        """Draws an info label in the middle of the window.

        This is shown on top of all the other window content while the translation is in progress.
        """
        wait_text = "Please wait patiently while the translation\n is requested from the online service"
        self._translation_label = ttk.Label(master=self._root, text=wait_text)
        self._translation_label.config(font=("Georgia", 20, "bold"),
                                      background='pink', justify="center")
        self._translation_label.place(relx=0.5, rely=0.5, anchor="center")
        self._translation_label.lift()


    def _handle_comboboxes(self, event):
        """Handler for message template comboboxes.

        Adds the selected combobox value in the end of the message text area.
        
        Args:
            event (Event ): An event caused by selection in one of the comboboxes
        """
        combobox = event.widget
        value = combobox.get()
        combobox.set(combobox.group_name)
        self._message_entry.insert('end', value)
        self._message_entry.see("end-1c")
        self._message_entry.mark_set("insert", "end-1c")
        self._message_entry.focus_set()


    def _handle_copy_button_click(self):
        """Handler for message copy button

        Checks that the message text is ready to be copied and copies it to clipboard.
        """
        entry_value = self._message_entry.get('1.0', 'end-1c')
        if self._checker.check_mandatory_fields_to_copy(entry_value) is True:
            self._root.clipboard_clear()
            self._root.clipboard_append(entry_value)


    def _handle_translate_button_click(self):
        """Handler for message translate button

        Gets the language selections and asks for translation from MessageTranslator.
        While the translation is in progress, shows an infolabel.
        After the translation is done, removes the info label, prints the translated tex into
        text area and returns the instruction texts back to the language selection comboboxes.
        """
        translate_from = self._translate_language_inputs[0].get()
        translate_to = self._translate_language_inputs[1].get()

        original_text = self._message_entry.get('1.0', 'end-1c')
        if original_text != "" and translate_from != "Translate from" and translate_to != "Translate to":
            self._draw_translation_label()
            self._root.update()
            translated_text = self._translator.translate_message(
                original_text, translate_from, translate_to)

            if translated_text is not None:
                self._message_entry.delete('1.0', 'end')
                self._message_entry.insert('1.0', translated_text)
                self._message_entry.mark_set("insert", "end-1c")
                self._message_entry.focus_set()

            self._translation_label.place_forget()
            self._translate_language_inputs[0].set("Translate from")
            self._translate_language_inputs[1].set("Translate to")


    def _handle_management_window_button_click(self):
        """Handler for management window opening button.

        Checks if the management window is allready open, and either activates it or opens a new one.
        """
        if self._management_window is None or not self._management_window.winfo_exists():
            self._management_window = ManagementWindow(
                self._root, self._message_handler, self.update_combobox_groups, self.update_combobox_contents)
            self._management_window.start()
        else:
            self._management_window.lift()


    def update_combobox_groups(self):
        """Updates the group names on the message template comboboxes.

        This method is given as a parameter to the management window so that it can ask the main 
        window to update group names when they are changed by the user.
        """
        self._group_names = self._message_handler.group_name_list()
        for i in range(8):
            self._comboboxes[i].set(self._group_names[i])


    def update_combobox_contents(self):
        """Updates the message templates in the comboboxes.

        This method is given as a parameter to the management window so that it can ask the main 
        window to update the comboboxes when the user changes the message texts.
        """
        self._message_texts = self._message_handler.all_message_texts_grouped()
        for i in range(8):
            self._comboboxes[i]['values'] = self._message_texts[i]
            self._comboboxes[i].set(self._group_names[i])
