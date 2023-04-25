# THERE WILL BE (HOPEFULLY) AN INFO WINDOW OPENING ABOUT
# THE STATUS OF THE TRANSLATION.
# I COULD NOT GET IT TO WORK IN TIME, SO THE RELATED LINES
# ARE COMMENTED OUT!!

from time import sleep
from googletrans import Translator, LANGUAGES, models
# from ui.ui_infowindow import InfoWindow
# from google_trans_new import google_translator
# from deep_translator import GoogleTranslator


class MessageTranslator:
    def __init__(self):

        self.translator = Translator(raise_exception=True)
        # self.translator = google_translator()
        # self.info_window = None

    def translate_message(self, text, language_from, language_to):
        language_code_from = self.get_language_code(language_from)
        language_code_to = self.get_language_code(language_to)
        result_translated = None
        result = None

        # if self.info_window is None:
        # title = "Translating..."
        # infotext = "Please wait patiently while the translation is requested "
        #   "from the online service"

        # self.info_window = InfoWindow(title, infotext, None, None, None, None)

        print("translate_message: language_code_from = ", language_code_from,
              ", language_code_to = ", language_code_to, ", text = \n ", text)

        for try_again in range(6):

            # Unfortunately it seems that googletrans library do not provide specific
            # exception classes, so have to use just "Exception" and ignore it for pylint!
            # Also, the googletrans library seems to work so unreliably that it's better
            # to catch all possible interrupts just in case.
            # pylint: disable=broad-except
            try:
                # result_translated = GoogleTranslator(
                # source=language_code_from, target=language_code_to).translate(text)
                result_translated = self.translator.translate(
                    text, language_code_to, language_code_from)
                if isinstance(result_translated, models.Translated):
                    result = result_translated.text
                    print("translate_message: result = ", result)
                    # self.info_window.close()
                    return result

            except Exception as error_message:
                # result = text + "\n\nTranslation failed: " + str(error_message)
                print("translate_message, try nr. ", try_again+1, ":  Translation failed: " +
                      str(error_message))
                sleep(2)

        # if self.info_window is None:
        # title = "Translating failed"
        # infotext = "Unfortunately, getting the translation from the online service "
        #   "was not successful!"
        # button1 = "Return"
        # button2 = "Try again"
        # self.info_window = InfoWindow(title, infotext, button1, button2, None, None)

        return None

    def get_language_code(self, language):
        for language_code, language_in_dict in LANGUAGES.items():
            if language == language_in_dict:
                return language_code
        return None

    def get_language_list(self):
        language_list = []
        language_list = list(LANGUAGES.values())
        return language_list
