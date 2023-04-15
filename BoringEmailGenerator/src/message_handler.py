from repositories.db_messages import MessageDB
from message import Message
from group import Group

class MessageHandler:
    def __init__(self, database):
        self.database = database
        self.groups = []


    def group_name_list(self):
    
        group_table = []
        group_names = self.database.get_groups()
    
        print("MessageHandler - group_list: group_names = ", group_names)

        for n in group_names:
            group_table.append(n[0])
        return group_table


    def all_messages_grouped(self):
        print("MessageHandler - all_messages_grouped")

        message_table = []
        for i in range(8):
            message_table.append(self.messages_by_group(i))

        #print('all_messages_grouped: ', message_table)
        return message_table


    def all_message_texts_grouped(self):
        print("MessageHandler - all_message_texts_grouped")
        messages_grouped = self.all_messages_grouped()


        message_texts_grouped_table = []
        for group in messages_grouped:
            message_text_table = []
            for message in group:
                message_text_table.append(message.text)
            message_texts_grouped_table.append(message_text_table)

        #print('all_message_texts_grouped: ', message_texts_grouped_table)
        return message_texts_grouped_table
    

    def messages_by_group(self, group_id):
        print("MessageHandler - rename_group: group = ", group_id)

        message_table = []
        messages = self.database.read_messages_from_group(group_id+1)

        for message in messages:
            message_table.append(Message(message[1], message[0]))
        
        return message_table


    def add_new_message(self, group_id, message_text):
        print("MessageHandler - add_new_message: group = ", group_id , ", text = ", message_text)
        self.database.insert_new_message(group_id+1, message_text)



    def rename_group(self, group_id, new_name):
        print("MessageHandler - rename_group: group = ", group_id , ", text = ", new_name)
        self.database.update_message_group_name(group_id+1, new_name)


    
    def delete_message(self, message):
        print("MessageHandler - delete_message: message = ", message, ", message_id = ", message.message_id)
        self.database.delete_message_by_id(message.message_id)