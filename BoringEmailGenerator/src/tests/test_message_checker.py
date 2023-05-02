import unittest
from message_checker import MessageChecker


class TestMessageChecker(unittest.TestCase):

    def setUp(self):
        self.checker = MessageChecker()

    def test_contains_mandatory_fields(self):
        message = "I am going to meet [NAME] on [date]."
        result = self.checker.contains_mandatory_field(message)
        expected = ['[NAME]', '[date]']

        self.assertEqual(result, expected)

    def test_not_contain_mandatory_fields(self):
        message = "Shetland ponies are the best."
        result = self.checker.contains_mandatory_field(message)
        expected = None

        self.assertEqual(result, expected)

    def test_check_mandatory_fields_to_copy_none_missing(self):
        message = "Shetland ponies are the best."
        result = self.checker.check_mandatory_fields_to_copy(message)
        expected = True

        self.assertEqual(result, expected)