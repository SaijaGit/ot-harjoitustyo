from tkinter import Tk
from ui.ui_mainwindow import MainWindow
from repositories.db_messages import MessageDB
from config import DATABASE
from message_handler import MessageHandler


# import sys
# from ui.ui_managementwindow import ManagementWindow

def main():
    # print(sys.path)
    # db_file = 'messages.db'
    database = MessageDB(DATABASE)
    message_handler = MessageHandler(database)

    window = Tk()
    window.title("Boring Email Generator")
    window.geometry('800x700')

    ui_main_window = MainWindow(window, message_handler)
    ui_main_window.start()

    window.mainloop()


if __name__ == "__main__":
    main()
