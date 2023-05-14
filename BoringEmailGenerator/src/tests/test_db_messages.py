import unittest
from repositories.db_messages import MessageDB
from config import TESTDATABASE


class TestMessageDB(unittest.TestCase):
    def setUp(self):
        self.database = MessageDB(TESTDATABASE)
        self.database.remove_table('message_groups')
        self.database.remove_table('messages')
        self.database.initialize_db()

    def test_db_group_intialization(self):
        groups_exist = self.database.table_exists('message_groups')

        self.assertEqual(groups_exist, True)

    def test_db_message_intialization(self):
        messages_exist = self.database.table_exists('messages')

        self.assertEqual(messages_exist, True)

    def test_table_exist_is_false_if_no_table(self):
        kissa_exist = self.database.table_exists('kissa')

        self.assertEqual(kissa_exist, False)

    def test_get_groups_returns_example_groups(self):
        groups = self.database.get_groups()
        self.assertEqual(len(groups), 8)

    def test_all_messages_returns_example_messages(self):
        messages = self.database.all_messages()
        self.assertEqual(len(messages), 24)

    def test_remove_table_removes_table(self):
        self.database.remove_table('messages')
        messages_exist = self.database.table_exists('messages')

        self.assertEqual(messages_exist, False)

    def test_get_groups_returns_right_groups(self):
        self.database.remove_table('message_groups')
        self.database.create_example_groups(['group1', 'group2'])
        groups = self.database.get_groups()
        self.assertEqual(groups, [('group1',), ('group2',)])

    def test_all_messages_returns_all_messages_in_one_table(self):
        self.database.remove_table('messages')
        self.database.create_example_messages([['m1', 'm2'], ['m3', 'm4']])
        messages = self.database.all_messages()
        self.assertEqual(messages, ['m1', 'm2', 'm3', 'm4'])
