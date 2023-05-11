
"""
This file provides example group names and message texts for the first use of a program,
or for the cases when the detabase file is destroyed or missing.
"""

def get_example_group_names():
    """
    Returns a list of example group names.
    """
    example_group_names = ["Greetings", "Inquiries", "Meetings",
                           "Sales", "Holidays", "Animals", "Miscellaneous", "Signatures"]
    return example_group_names


def get_example_message_texts():
    """
    Returns a list of example message texts.
    """

    whale = r'''
          .':'.
         ___:____     |¨\/¨|
       ,'        `.    \  /
       |  O        \___/  |
    ~^~^~^~^~^~^~^~^~^~^~^~^~ 

    '''
    hippo = r'''
          c~~p ,---------.
     ,---'oo  )            \
    ( O O                   )/
      `=^='                 /
           \    ,     .    /
            \\  |----'|   /
            ||__|   |_|__|

    '''

    cat = r'''
      _._     _,-'""`-._
     (,-.`._,'(       |\`-/|
         `-.-' \ )-`( , o o)
               `-    \`_`*'- 

    '''

    example_message_texts = [["\nHello [RECIPIENT], \nI hope you're having a fantastic day! ",
                              "\nDear [RECIPIENT], \nI’m reaching out to you because … ",
                              "\nHi [RECIPIENT],\nand thank you for your quick response! "],

                             ["\nDear [RECIPIENT], \nThank you for your inquiry about our "
                              "products. I have attached further information on our products "
                              "to this email. "
                              "Please feel free to review the attached documents and let me "
                              "know if you have any further questions or if you require "
                              "additional information.",
                             "\nReferring to our recent telephone conversation,\n",
                              "\nHello, \nand thank you for your interest in our company's "
                              "products! "
                              "As an attachment you will find ...",
                              "\nDear [RECIPIENT], \nThank you for taking the time to speak "
                              "with me today about [TOPIC]. I would like to request "
                              "additional information regarding ..."],

                             ["\nI'm writing to ask if you have any availability for a "
                              "meeting next week.",
                              "\nI wanted to thank you for the opportunity to meet with you "
                              "today and discuss [TOPIC]. It was a pleasure to learn more "
                              "about [TOPIC] and how we might be able to work together."],

                             ["\nHello [RECIPIENT], and thanks for the request for a quote! "
                              "sWe are pleased to offer you",
                              "\nAll prices are exclusive of VAT. Shipping costs will be "
                              "invoiced based on actual expenses.",
                              "\nThank you for your order! We appreciate your trust and "
                              "look forward to delivering your order as soon as possible. ",
                              "\nThe delivery time is currently about 3 weeks. "],

                             ["\nOur office will be closed from [DATE] to [DATE] for the "
                              "Christmas holidays. In the meantime, we would like to wish you "
                              "and your loved ones a Merry Christmas and a Happy New Year! ",
                              "\nWishing you a great Halloween and a fantastic fall! "],

                             [whale, hippo, cat],

                             ["\nFirst 100 decimal places of pi are 3,14159 26535 89793 "
                              "23846 26433 83279 50288 41971 69399 37510 58209 74944 "
                              "59230 78164 06286 20899 86280 34825 34211 70679.",
                              "\nShetland ponies are not only incredibly adorable, but they "
                              "also make great pets and companions. They are known for their "
                              "hardy and resilient nature, and they are surprisingly strong "
                              "considering that they are usually only about a meter tall. "
                              "They are intelligent and eager to please, making them great for "
                              "training and learning new tricks. Shetland ponies are a wonderful "
                              "addition to any family and are sure to bring joy and happiness to "
                              "those who have the pleasure of owning one.",
                              "\nWhen a cowplant gets hungry, a piece of cake appears hanging "
                              "from its mouth. If you grab the cake to eat it, the cowplant will "
                              "swallow you. On the first time notehing really bad happens, as the "
                              "cowplant just spits you back out. But if you try to get the cake "
                              "again in a short time, you will be swallowed by the cowplant and "
                              "never seen again."],

                             ["\nThank you for your time and consideration. I look forward to "
                              "hearing back from you soon.\nBest regards,\n",
                              "\nPlease let me know if you have any questions or if there is "
                              "anything else I can provide to help move this project forward. "
                              "I look forward to hearing back from you soon. \nKind regards, \n",
                              "\nSo long and thanks for all the fish!"]]

    return example_message_texts
