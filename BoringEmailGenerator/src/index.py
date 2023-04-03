from tkinter import Tk
from ui.ui_mainwindow import UI
from repositories.db_messages import MessageDB
from config import DATABASE


def main():

    #db_file = 'messages.db'
    database = MessageDB(DATABASE)

    window = Tk()
    window.title("Boring Email Generator")
    window.geometry('800x600')

    ui = UI(window, database)
    ui.start()

    database.get_groups()
    database.all_messages()
    database.messages_by_group(1)

    window.mainloop()




if __name__ == "__main__":
    main()