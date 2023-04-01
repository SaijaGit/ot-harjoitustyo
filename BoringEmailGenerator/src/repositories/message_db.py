import sqlite3

class MessageDB:
    def __init__(self):
        self.db_connection = sqlite3.connect('messages.db')
        self.cursor = self.db_connection.cursor()
        self.initialize_db()


    def initialize_db(self):

        if not self.table_exists("messages") :
            self.create_example_messages()

        if not self.table_exists("message_groups") :
            self.create_example_groups()
        
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
            print(texts_table)
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
        
    
    def create_example_groups(self):
        group_names = ["Greetings", "Inquiries", "Meetings", "Sales", "Orders", "Animals", "Miscellaneous", "Signatures"]

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS message_groups (id INTEGER PRIMARY KEY AUTOINCREMENT, group_id INTEGER UNIQUE, name TEXT)''')

        for i in range(1, 9):
            self.cursor.execute('INSERT INTO message_groups (group_id, name) VALUES (?, ?)', (i, group_names[i-1]))

        self.db_connection.commit()


    def create_example_messages(self):


        message_texts = [["\nHello [RECIPIENT], \nI hope you're having a fantastic day! ", 
                            "\nDear [RECIPIENT], \nI’m reaching out to you because … ", 
                            "\nHi [RECIPIENT],\nand thank you for your quick response! "] ,
                            
                            ["\nDear [RECIPIENT], \nThank you for your inquiry about our products. I have attached further information on our products to this email. Please feel free to review the attached documents and let me know if you have any further questions or if you require additional information.", 
                            "\nPlease let me know if you have any questions or if there is anything else I can provide to help move this project forward. I look forward to hearing back from you soon.",
                            "\nHello, \nand thank you for your interest in our company's products! As an attachment you will find ...", 
                            "\nDear [RECIPIENT], \nThank you for taking the time to speak with me today about [TOPIC]. I would like to request additional information regarding ..."],
                            
                            ["\nI'm writing to ask if you have any availability for a meeting next week.", 
                             "\nI wanted to thank you for the opportunity to meet with you today and discuss [TOPIC]. It was a pleasure to learn more about [TOPIC] and how we might be able to work together."],
                             
                            ["\nHello [RECIPIENT], and thanks for the request for a quote! We are pleased to offer you", 
                             "\nAll prices are exclusive of VAT. Shipping costs will be invoiced based on actual expenses.", 
                             "\nThank you for your order! We appreciate your trust and look forward to delivering your order as soon as possible. ", 
                             "\nThe delivery time is currently about 3 weeks. "],
                            
                            ["Our office will be closed from [DATE] to [DATE] for the Christmas holidays. In the meantime, we would like to wish you and your loved ones a Merry Christmas and a Happy New Year! ",
                             "Wishing you a great Halloween and a fantastic fall! "],
                             
                            ["\n     .':'.\n    ___:____     |¨\/¨|\n  ,'        `.    \  /\n  |  O        \___/  |\n~^~^~^~^~^~^~^~^~^~^~^~^~", 
                             "\n      c~~p ,---------. \n ,---'oo  )           \ \n( O O                  )/ \n `=^='                 / \n       \    ,     .   / \n       \ \  |----'|  /\n       ||__|    |_|__|",
                             "\n _._     _,-'""`-._ \n(,-.`._,'(       |\`-/| \n    `-.-' \ )-`( , o o) \n          `-    \`_`*'- "],
                            
                            ["\nFirst 100 decimal places of pi are 3,14159 26535 89793 23846 26433 83279 50288 41971 69399 37510 58209 74944 59230 78164 06286 20899 86280 34825 34211 70679.", 
                             "\nShetland ponies are not only incredibly adorable, but they also make great pets and companions. They are known for their hardy and resilient nature, and they are surprisingly strong. They are intelligent and eager to please, making them great for training and learning new skills. Overall, Shetland ponies are a wonderful addition to any family and are sure to bring joy and happiness to those who have the pleasure of owning one.",
                             "\nWhen a cowplant gets hungry, a piece of cake appears hanging from its mouth. If you grab the cake to eat it, the cowplant will swallow you. On the first time notehing really bad happens, as the cowplant just spits you back out. But if you try to get the cake again in a short time, you will be swallowed by the cowplant and never seen again."],
                            
                            ["\nThank you for your time and consideration. I look forward to hearing back from you soon.\nBest regards",
                             "\nPlease let me know if you have any questions or if there is anything else I can provide to help move this project forward. I look forward to hearing back from you soon. Kind regards",
                             "\nSo long and thanks for all the fish!"]]
        
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY AUTOINCREMENT, message_group INTEGER, text TEXT)''')
        
        i = 0
        for group in message_texts :
            i += 1
            for message in group :
                self.cursor.execute('INSERT INTO messages (message_group, text) VALUES (?, ?)', (i, message))
        
        self.db_connection.commit()

