from entities.message import Message


class MessageHandler:
    """Passes data and requests between ui and the database writer class MessageDB.

    The MessageHandler class works between the gui classes and the MessageDB class
    that is responsible for writing the actual sql queries.
    It forwards requests from the gui to the MessageDB and converts the data received
    from the database into the format needed by the gui.
    """

    def __init__(self, database_writer):
        """Initiates the MessageHandler class.

        Args:
            database_writer (MessageDB): An instance of the MessageDB class responsible 
            for the database operations.
        """
        self._database_writer = database_writer


    def group_name_list(self):
        """Passes all the group names in a list.

        Returns:
            list: A list of group names.
        """
        group_table = []
        group_names = self._database_writer.get_groups()

        for group in group_names:
            group_table.append(group[0])
        return group_table


    def all_messages_grouped(self):
        """Get all message template objects.

        Passes all the message objects in a 2-dimensional list, that contains separate 
        lists for the messages of each group.

        Returns:
            list: A  list of message objects grouped.
        """
        message_table = []
        for i in range(8):
            message_table.append(self.messages_by_group(i))

        return message_table


    def all_message_texts_grouped(self):
        """Get all message template texts.
        
        Passes all the message template texts in a 2-dimensional list, that contains
        separate lists for the messages of each group.

        Returns:
            list: A  list of message texts grouped.
        """
        messages_grouped = self.all_messages_grouped()

        message_texts_grouped_table = []
        for group in messages_grouped:
            message_text_table = []
            for message in group:
                message_text_table.append(message.text)
            message_texts_grouped_table.append(message_text_table)

        return message_texts_grouped_table


    def messages_by_group(self, group_id):
        """Passes the message objects of a given group.

        Args:
            group_id (int): Group id (range 0...7)

        Returns:
            list: A  list of message objects
        """
        message_table = []
        messages = self._database_writer.read_messages_from_group(group_id+1)

        for message in messages:
            message_table.append(Message(message[1], message[0]))

        return message_table


    def rename_group(self, group_id, new_name):
        """Asks MessageDB to update a group name in the database.

        Args:
            group_id (int): Group id (range 0...7)
            new_name (str): New name for the group
        """
        self._database_writer.update_message_group_name(group_id+1, new_name)


    def delete_message(self, message):
        """Asks MessageDB to delete a message template from the database.

        Args:
            message (Message): A message object to be removed
        """
        self._database_writer.delete_message_by_id(message.message_id)


    def update_message(self, message, message_text):
        """Asks MessageDB to update a texts of a message template in the database.

        Args:
            message (Message): A message object to be updated
            message_text (str): New text for the message template
        """
        self._database_writer.update_message_text(message.message_id, message_text)


    def add_new_message(self, group_id, message_text):##
        """Asks MessageDB to add a new message template to the database.

        Args:
            group_id (int): Group id (range 0...7) for the new message template
            message_text (str): Text for the new message template
        """
        self._database_writer.insert_new_message(group_id+1, message_text)
