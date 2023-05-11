import sqlite3
from .db_example_messages import get_example_group_names, get_example_message_texts


class MessageDB:
    """
    A class for handling the sqlite database, that the program uses to store 
    message templates.

    """

    def __init__(self, db_file):
        """
        Sets up the connection to the database ans calls for initialization of 
        the database.

        Args:
            db_file (str): The name of the file where the database is saved 
        """
        
        self.db_connection = sqlite3.connect(db_file)
        self.cursor = self.db_connection.cursor()
        self.message_id_vs_place = {}
        self.initialize_db()


    def initialize_db(self):
        """
        Makes sure that the database tables required for the using the 
        program exist.
        If they dont exist, gets the example group names and message texts
        from db_example_messages.
        """
        if not self.table_exists("messages"):
            example_message_texts = get_example_message_texts()
            self.create_example_messages(example_message_texts)

        if not self.table_exists("message_groups"):
            example_group_names = get_example_group_names()
            self.create_example_groups(example_group_names)


    def table_exists(self, tablename):
        """
        Checks that a certain database table exists.

        Args:
            tablename (str): The name of the table to be checked

        Returns:
            bool: True if the table exists, False otherwise.
        """
        query = '''
                SELECT name
                FROM sqlite_master
                WHERE type=?
                AND name=?
                '''
        self.cursor.execute(query, ('table', tablename))

        name = self.cursor.fetchone()
        if name is not None:
            return True

        return False
    
    
    def create_example_groups(self, example_group_names):
        """
        Creates a database table with example groups names.

        Args:
            example_group_names (list): A list of example group names
        """
        query = '''
                CREATE TABLE IF NOT EXISTS message_groups (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    group_id INTEGER UNIQUE,
                    name TEXT
                )
                '''
        self.cursor.execute(query)

        for i in range(1, len(example_group_names)+1):
            query = '''
                    INSERT INTO message_groups (group_id, name)
                    VALUES (?, ?)
                    '''
            self.cursor.execute(query, (i, example_group_names[i-1]))

        self.db_connection.commit()


    def create_example_messages(self, example_message_texts):
        """
        Creates a database table with example message templates.

        Args:
            example_message_texts (list): A list of example message texts
        """
        query = '''
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                message_group INTEGER, 
                text TEXT
            )
            '''
        self.cursor.execute(query)

        group_id = 0
        for group in example_message_texts:
            group_id += 1
            for message in group:
                query = """
                    INSERT INTO messages (message_group, text)
                    VALUES (?, ?)
                """
                self.cursor.execute(query, (group_id, message))

        self.db_connection.commit()


    def remove_table(self, tablename):
        """
        Removes a table from the database.

        Args:
            tablename (str): The name of the table to be removed
        """
        query = f"DROP TABLE IF EXISTS {tablename}"
        self.cursor.execute(query)
        self.db_connection.commit()


    def get_groups(self):
        """
        Gets a list of group names from the database.

        Returns:
            list: Group names
        """
        if self.table_exists("message_groups"):
            query = '''SELECT name FROM message_groups'''
            self.cursor.execute(query)
            group_names = self.cursor.fetchall()
            return group_names
        return None


    def all_messages(self):
        """
        Gets all message templates from the database.

        Returns:
            list: All message texts
        """
        if self.table_exists("messages"):
            query = '''SELECT text FROM messages'''
            self.cursor.execute(query)
            messages = self.cursor.fetchall()
            texts_table = []

            for message in messages:
                texts_table.append(message[0])

            return texts_table
        return None
    

    def read_messages_from_group(self, group_id):
        """
        Gets all message templates from a certain group.

        Args:
            group_id (int): the ID of the group

        Returns:
            list: messages belonging to the group
        """
        if self.table_exists("messages"):

            query = '''
                    SELECT text, id
                    FROM messages
                    WHERE message_group=?
                    '''
            self.cursor.execute(query, (group_id,))
            messages = self.cursor.fetchall()
            return messages
        return None


    def insert_new_message(self, group_id, message_text):
        """
        Writes a new message template into the database.

        Args:
            group_id (int): The id of the group of the message to be added
            message_text (str): The text of the new message
        """
        query = '''
                CREATE TABLE IF NOT EXISTS messages (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    message_group INTEGER, 
                    text TEXT
                )
                '''
        self.cursor.execute(query)

        query = '''
                INSERT INTO messages (
                    message_group, text
                ) 
                VALUES (?, ?)
                '''
        self.cursor.execute(query, (group_id, message_text))

        self.db_connection.commit()


    def update_message_group_name(self, group_id, name):
        """
        Updates the name of a group into the database group table.

        Args:
            group_id (int): id of the group to be updated
            name (str): the new name for the group
        """
        if self.table_exists("message_groups"):
            query = '''
                    UPDATE message_groups 
                    SET name=? 
                    WHERE group_id=?
                    '''
            self.cursor.execute(query, (name, group_id))
            self.db_connection.commit()


    def update_message_text(self, message_id, text):
        """
        Updates the text of an existing message template.

        Args:
            message_id (int): the id of the message to be updated
            text (str): the new text for the message
        """
        if self.table_exists("messages"):
            query = '''
                    UPDATE messages 
                    SET text=? 
                    WHERE id=?
                    '''
            self.cursor.execute(query, (text, message_id))
            self.db_connection.commit()


    def get_group_name(self, group_id):
        """
        Gets the name of a group with a certain id.

        Args:
            group_id (int): id of the group

        Returns:
            str: the name of the group
        """
        if self.table_exists("message_groups"):
            query = '''
                    SELECT name 
                    FROM message_groups 
                    WHERE group_id=?
                    '''
            self.cursor.execute(query, (group_id,))
            group_name = self.cursor.fetchone()

            if group_name is not None:
                return group_name[0]
        return None
    

    def delete_message_by_id(self, message_id):
        """
        Deletes a message with the certain ID from the database.

        Args:
            group_id (int): id of the message to be deleted
        """
        if self.table_exists("messages"):
            query = '''
                    DELETE FROM messages 
                    WHERE id=?
                    '''
            self.cursor.execute(query, (message_id,))

            self.db_connection.commit()
