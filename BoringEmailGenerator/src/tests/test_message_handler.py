import unittest
from repositories.db_messages import MessageDB
from services.message_handler import MessageHandler
from config import TESTDATABASE


class TestMessageHandler(unittest.TestCase):
    def setUp(self):
        database = MessageDB(TESTDATABASE)
        database.remove_table('message_groups')
        database.remove_table('messages')
        database.initialize_db()

        self.message_handler = MessageHandler(database)

    def test_group_name_list(self):
        group_table = self.message_handler.group_name_list()
        expected = ['Greetings', 'Inquiries', 'Meetings',
                    'Sales', 'Holidays', 'Animals',
                    'Miscellaneous', 'Signatures']

        self.assertEqual(group_table, expected)

    def test_all_message_texts_grouped(self):
        message_texts_grouped = self.message_handler.all_message_texts_grouped()

        result = (
            len(message_texts_grouped),
            message_texts_grouped[0][0],
            message_texts_grouped[1][1],
            message_texts_grouped[2][0],
            message_texts_grouped[3][3],
            message_texts_grouped[4][1],
            len(message_texts_grouped[5][2]),
            message_texts_grouped[6][0],
            message_texts_grouped[7][2]
        )

        expected = (
            8,
            "\nHello [RECIPIENT], \nI hope you're having a fantastic day! ",
            "\nReferring to our recent telephone conversation,\n",
            "\nI'm writing to ask if you have any availability for a "
            "meeting next week.",
            "\nThe delivery time is currently about 3 weeks. ",
            "\nWishing you a great Halloween and a fantastic fall! ",
            119,
            "\nFirst 100 decimal places of pi are 3,14159 26535 89793 "
            "23846 26433 83279 50288 41971 69399 37510 58209 74944 "
            "59230 78164 06286 20899 86280 34825 34211 70679.",
            "\nSo long and thanks for all the fish!"
        )

        self.assertEqual(result, expected)

    def test_rename_group(self):
        self.message_handler.rename_group(1, "Pulla")
        result = self.message_handler.group_name_list()[1]
        expected = "Pulla"
        self.assertEqual(result, expected)

    def test_delete_message(self):
        messages_before = self.message_handler.messages_by_group(2)
        amount_before = len(messages_before)
        message_1_before_id = messages_before[1].message_id
        message_1_before_text = messages_before[1].text
        self.message_handler.delete_message(messages_before[0])
        messages_after = self.message_handler.messages_by_group(2)
        amount_after = len(messages_after)
        message_0_after_id = messages_after[0].message_id
        message_0_after_text = messages_after[0].text

        result = (
            amount_before,
            message_0_after_id,
            message_0_after_text,
            amount_after
        )

        expected = (
            2,
            message_1_before_id,
            message_1_before_text,
            1
        )

        self.assertEqual(result, expected)

    def test_update_message(self):
        message_before = self.message_handler.messages_by_group(4)[1]
        self.message_handler.update_message(message_before, "Kakku")
        message_after = self.message_handler.messages_by_group(4)[1]

        result = (
            message_after.text,
            message_after.message_id
        )

        expected = (
            "Kakku",
            message_before.message_id
        )

        self.assertEqual(result, expected)

    def test_add_new_message(self):
        messages_before = self.message_handler.messages_by_group(5)
        amount_before = len(messages_before)
        self.message_handler.add_new_message(5, "Hello World!")
        messages_after = self.message_handler.messages_by_group(5)
        amount_after = len(messages_after)

        result = (
            amount_after,
            messages_after[amount_after-1].text,
        )

        expected = (
            amount_before + 1,
            "Hello World!",
        )

        self.assertEqual(result, expected)
