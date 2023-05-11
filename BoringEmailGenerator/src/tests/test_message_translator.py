import unittest
from time import sleep
from unittest.mock import patch
from services.message_translator import MessageTranslator


class TestMessageTranslator(unittest.TestCase):
    def setUp(self):
        self.translator = MessageTranslator()

    def test_translate_message(self):
        for test_times in range(10):
            with patch('services.message_translator.messagebox.askretrycancel', return_value='True'):
                result = self.translator.translate_message(
                    'cat',  'english', 'finnish')
                sleep(5)
                if result is not None:
                    break

        expected = 'kissa'

        self.assertEqual(result, expected)

    def test_translate_message_exception_false(self):
        with patch('services.message_translator.Translator.translate') as mock_exception:
            with patch('services.message_translator.messagebox.askretrycancel') as mock_message_box:
                mock_exception.side_effect = Exception("Translation failed!")
                mock_message_box.return_value = False

                result = self.translator.translate_message(
                    'cat', 'english', 'finnish')
                expected = None

                self.assertEqual(result, expected)

    def test_get_language_code_good(self):
        result = self.translator.get_language_code('english')
        expected = 'en'

        self.assertEqual(result, expected)

    def test_get_language_code_invalid(self):
        result = self.translator.get_language_code('123456789')
        expected = None

        self.assertEqual(result, expected)

    def test_get_language_list(self):
        list = self.translator.get_language_list()
        result = [list[0], list[1], list[2]]
        expected = ['afrikaans', 'albanian', 'amharic']

        self.assertEqual(result, expected)
