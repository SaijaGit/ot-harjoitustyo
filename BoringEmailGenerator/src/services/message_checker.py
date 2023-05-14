import re
from tkinter import messagebox


class MessageChecker:
    """Check the message for missing data.

    Class for checking if a message text contains substrings that may be in the message 
    to mark missing mandatory data and warn the user before copying it to be used in 
    their email app.
    """

    def __init__(self):
        """Initializes MessageChecker.

        Defines a regular expression pattern for identifying mandatory fields.
        The substring is suspected to be marking a mandatory field, if it contains 1-20
        characters between []-brackets.
        """
        self._mandatory_field = r'\[[\w\d\s]{1,20}\]'


    def check_mandatory_fields_to_copy(self, message_text):
        """Check the message and notify the user if data missing.

        Checks if message_text contains mandatory fields, and if they are found,
        opens a message box that informs the user with a list of suspected mandatory fields,
        and asks user to click yes or no for continuing the copying. 

        Args:
            message_text (str): The text of the message to check.

        Returns:
            bool: True if the user chooses to continue, and False otherwise.
        """
        missing_fields = self.contains_mandatory_field(message_text)
        if missing_fields:
            fields_text = ', '.join(missing_fields)
            error_text = (
                f"The message contains the following mandatory fields:\n{fields_text}"
                "\n\nDo you still want to copy the message? "
            )

            button_result = messagebox.askquestion(
                "Check the message for missing information!",
                error_text
            )
            if button_result == "no":
                return False

        return True

    def contains_mandatory_field(self, message_text):
        """Search any mandatory data fields from the text.

        Searches for and returns a list of suspected mandatory fields found 
        from the message text.

        Args:
            message_text (str): The text of the message to search for mandatory fields

        Returns:
            list or None: A list of suspected mandatory fields found in the message_text,
            or None if none were found
        """
        found_fields = re.findall(self._mandatory_field, message_text)
        if found_fields:
            return found_fields

        return None
