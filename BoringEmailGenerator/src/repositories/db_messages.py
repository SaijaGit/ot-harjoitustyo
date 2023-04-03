import sqlite3
from .db_example_messages import get_example_group_names, get_example_message_texts

class MessageDB:
    def __init__(self, db_file):
        self.db_connection = sqlite3.connect(db_file)
        self.cursor = self.db_connection.cursor()
        self.initialize_db()


    def initialize_db(self):

        if not self.table_exists("messages") :
            example_message_texts = get_example_message_texts()
            self.create_messages(example_message_texts)

        if not self.table_exists("message_groups") :
            example_group_names = get_example_group_names()
            self.create_groups(example_group_names)
        
        #self.cursor.close()




    def table_exists(self, tablename):
        #tablename = "kissa"
        self.cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{tablename}'")

        name = self.cursor.fetchone()
        print("Found table: name = ", name)
        if name != None :
            print("Table exists: ", tablename)
            return True

        print("Table doesn't exist: ", tablename)
        return False


    def remove_table(self, tablename):
        self.cursor.execute(f"DROP TABLE IF EXISTS {tablename}")
        self.db_connection.commit()



    def get_groups(self) :
        if self.table_exists("message_groups") :
            self.cursor.execute('SELECT name FROM message_groups')
            group_names = self.cursor.fetchall()
            group_table = []
            print(group_names)
            for n in group_names:
                group_table.append(n[0])
            print(group_table)
            return group_table
        
    

    def all_messages(self) :
        if self.table_exists("messages") :
            self.cursor.execute('SELECT text FROM messages')
            texts = self.cursor.fetchall()
            texts_table = []
            print(texts)
            for t in texts:
                texts_table.append(t[0])
            print('all_messages: ', texts_table)
            return texts_table 

    def messages_by_group(self, group_id) :
        if self.table_exists("messages") :
            self.cursor.execute(f"SELECT text FROM messages WHERE message_group='{group_id}'")
            texts = self.cursor.fetchall()
            texts_table = []
            print(texts)
            for t in texts:
                texts_table.append(t[0])
            print(texts_table)
            return texts_table 
        
    
    def create_groups(self, example_group_names):

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS message_groups (id INTEGER PRIMARY KEY AUTOINCREMENT, group_id INTEGER UNIQUE, name TEXT)''')

        for i in range(1, len(example_group_names)+1):
            self.cursor.execute('INSERT INTO message_groups (group_id, name) VALUES (?, ?)', (i, example_group_names[i-1]))

        self.db_connection.commit()


    def create_messages(self, example_message_texts):   
        
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY AUTOINCREMENT, message_group INTEGER, text TEXT)''')
        
        i = 0
        for group in example_message_texts :
            i += 1
            for message in group :
                self.cursor.execute('INSERT INTO messages (message_group, text) VALUES (?, ?)', (i, message))
        
        self.db_connection.commit()

