import re
from tkinter import messagebox


class MessageChecker:

    """
    Class for checking if a message text contains mandatory fields

    Attributes:
        mandatory_field (str): Regular expression pattern for identifying substrings that 
        may be in the message to mark mandatory fields.
        The substring is suspected to be marking a mandatory field, if it contains 1-20
        characters between []-brackets.

    Methods:
        check_mandatory_fields_to_copy(message_text): Checks if message_text contains 
            mandatory fields, and prompts the user to continue or cancel the copying. 
            Returns True if the user chooses to continue, and False otherwise.

        contains_mandatory_field(message_text): Searches for and returns a list of 
            possible mandatory fields found in the message_text.
    """

    def __init__(self):
        self.mandatory_field = r'\[[\w\d\s]{1,20}\]'

    def check_mandatory_fields_to_copy(self, message_text):
        """
        Checks if message_text contains mandatory fields, and if they are found,
        opens a message box that informs the user with a list of suspected
        mandatory fields, and asks user to click yes or no for continuing
        the copying. 

        Args:
            message_text (str): The text of the message to check.

        Returns:
            bool: True if the user chooses to continue, and False otherwise.
        """
        missing_fields = self.contains_mandatory_field(message_text)
        if missing_fields is not None:
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
        """
        Searches for and returns a list of suspected mandatory fields found 
        from the message_text.

        Args:
            message_text (str): The text of the message to search for mandatory fields

        Returns:
            list or None: A list of suspected mandatory fields found in the message_text,
            or None if none were found
        """
        found_fields = re.findall(self.mandatory_field, message_text)
        if len(found_fields) != 0:
            return found_fields

        return None
