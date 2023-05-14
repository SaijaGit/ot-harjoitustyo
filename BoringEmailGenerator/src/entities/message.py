class Message:
    """
    The Message class represents a message template with an ID for database and text content.

    Attributes:
        - message_id (int): The unique identifier for the message.
        - text (str): The content of the message.
    """

    def __init__(self, message_id, text):
        self.message_id = message_id
        self.text = text
