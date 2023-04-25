import unittest
from time import sleep
from message_translator import MessageTranslator


class TestMessageTranslator(unittest.TestCase):
    def setUp(self):
        self.translator = MessageTranslator()

    def test_translate_message(self):
        for test_times in range(10):
            result = self.translator.translate_message(
                'cat',  'english', 'finnish')
            sleep(5)
            if result is not None:
                break

        expected = 'kissa'

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
