from time import sleep
from tkinter import messagebox
from googletrans import Translator, LANGUAGES, models
# from ui.ui_infowindow import InfoWindow
# from ui.styles import configure_messagebox_style


class MessageTranslator:
    """A class for translating messages using a free Google Translate 
        library called googletrans.
    """

    def __init__(self):
        """Initialize a new instance of the MessageTranslator class."""

        self.translator = Translator(raise_exception=True)
        # self.info_window = None
        # configure_messagebox_style()

    def translate_message(self, text, language_from, language_to):
        """Translate a message from one language to another.
            If the translation fails, it is tried max 6 times, and then 
            a message box is opened to ask the user wether they want to cancel or
            try again.

        Args:
            text (str): The message text to be translated.
            language_from (str): The language code of the original language of the message.
            language_to (str): The language code of the target language for the translation.

        Returns:
            str: The translated message, or None if the translation failed.
        """

        language_code_from = self.get_language_code(language_from)
        language_code_to = self.get_language_code(language_to)
        result_translated = None
        result = None
        try_again = 0

        while try_again < 6:

            # Unfortunately it seems that googletrans library do not provide specific
            # exception classes, so have to use just "Exception" and ignore it for pylint!
            # Also, the googletrans library seems to work so unreliably that it's better
            # to catch all possible interrupts just in case.
            # pylint: disable=broad-except
            try:
                result_translated = self.translator.translate(
                    text, language_code_to, language_code_from)
                if isinstance(result_translated, models.Translated):
                    result = result_translated.text
                    return result

            except Exception as error_message:
                try_again += 1
                print("translate_message, try nr. ", try_again, ":  Translation failed: " +
                      str(error_message))

                if try_again == 6:
                    error_text = (
                        "Unfortunately the translation could not be completed. "
                        "Do you want to cancel or try again?")

                    button_result = messagebox.askretrycancel(
                        "Translation failed",
                        error_text
                    )

                    if not button_result:
                        break

                    try_again = 0

                sleep(2)

        return None

    def get_language_code(self, language):
        """Get the language code that mathces the language name.

        Args:
            language (str): The name of the language.

        Returns:
            str: The language code, or None if there was no such language found.
        """
        for language_code, language_in_dict in LANGUAGES.items():
            if language == language_in_dict:
                return language_code
        return None

    def get_language_list(self):
        """Get a list of the names of the languages that are supported.

        Returns:
            list: A list of supported language names.
        """
        language_list = []
        language_list = list(LANGUAGES.values())
        return language_list
