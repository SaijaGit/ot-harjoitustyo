import sqlite3
from .db_example_messages import get_example_group_names, get_example_message_texts


class MessageDB:
    def __init__(self, db_file):
        self.db_connection = sqlite3.connect(db_file)
        self.cursor = self.db_connection.cursor()
        self.message_id_vs_place = {}
        self.initialize_db()


    def initialize_db(self):

        if not self.table_exists("messages"):
            example_message_texts = get_example_message_texts()
            self.create_example_messages(example_message_texts)

        if not self.table_exists("message_groups"):
            example_group_names = get_example_group_names()
            self.create_example_groups(example_group_names)


        # self.cursor.close()

    def table_exists(self, tablename):
        # tablename = "kissa"
        self.cursor.execute(
            f"SELECT name FROM sqlite_master WHERE type='table' AND name='{tablename}'")

        name = self.cursor.fetchone()
        print("Found table: name = ", name)
        if name != None:
            print("Table exists: ", tablename)
            return True

        print("Table doesn't exist: ", tablename)
        return False

    def remove_table(self, tablename):
        self.cursor.execute(f"DROP TABLE IF EXISTS {tablename}")
        self.db_connection.commit()

    def get_groups(self):
        if self.table_exists("message_groups"):
            self.cursor.execute('SELECT name FROM message_groups')
            group_names = self.cursor.fetchall()
            return group_names

    def all_messages(self):
        if self.table_exists("messages"):
            self.cursor.execute('SELECT text FROM messages')
            texts = self.cursor.fetchall()
            texts_table = []
            print(texts)
            for t in texts:
                texts_table.append(t[0])
            print('all_messages: ', texts_table)
            return texts_table


    def read_messages_from_group(self, group_id):
        if self.table_exists("messages"):
            self.cursor.execute(
                f"SELECT text, id FROM messages WHERE message_group='{group_id}'")
            messages = self.cursor.fetchall()
            return messages

    def create_example_groups(self, example_group_names):

        self.cursor.execute(
            '''CREATE TABLE IF NOT EXISTS message_groups (id INTEGER PRIMARY KEY AUTOINCREMENT, group_id INTEGER UNIQUE, name TEXT)''')

        for i in range(1, len(example_group_names)+1):
            self.cursor.execute(
                'INSERT INTO message_groups (group_id, name) VALUES (?, ?)', (i, example_group_names[i-1]))

        self.db_connection.commit()

    def create_example_messages(self, example_message_texts):

        self.cursor.execute(
            '''CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY AUTOINCREMENT, message_group INTEGER, text TEXT)''')

        i = 0
        for group in example_message_texts:
            i += 1
            for message in group:
                self.cursor.execute(
                    'INSERT INTO messages (message_group, text) VALUES (?, ?)', (i, message))

        self.db_connection.commit()


    def insert_new_message(self, group_id, message_text):

        self.cursor.execute(
            '''CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY AUTOINCREMENT, message_group INTEGER, text TEXT)''')

        self.cursor.execute(
            'INSERT INTO messages (message_group, text) VALUES (?, ?)', (group_id, message_text))

        self.db_connection.commit()





    def update_message_group_name(self, group_id, name):
        if self.table_exists("message_groups"):
            self.cursor.execute(
                f"UPDATE message_groups SET name=? WHERE group_id=?", (name, group_id))
            self.db_connection.commit()
            print("update_message_group_name: group = ", group_id, ", name = ", name)

            #self.get_group_name(group_id)


    
    def get_group_name(self, group_id):
    
        if self.table_exists("message_groups"):
            self.cursor.execute(
                f"SELECT name FROM message_groups WHERE group_id='{group_id}'")
            group_name = self.cursor.fetchone()
            print("get_group_name: group = ", group_id, ", name = ", group_name[0])
            if group_name is not None:
                return group_name[0]
        return None
    

    def delete_message_by_id(self, id):
    
        if self.table_exists("messages"):
            self.cursor.execute(
                f"DELETE FROM messages WHERE id='{id}'")
            print("delete_message_by_id: id = ", id)
            self.db_connection.commit()

