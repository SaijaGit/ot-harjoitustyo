# Arkkitehtuurikuvaus

## Rakenne

Ohjelman koodi on tällä hetkellä jaettu kansioihin seuraavasti: 

src 
 - sisältää tiedoston index.py, jossa on main-luuppi ja joka käynnistää käyttöliittymän ja tietokannan
 - message_handler.py hoitaa tiedon käsittelyn ja siirron käyttöliittymän ja tietokantaa hoitavan luokan MessageDB välillä
 - message.py: Message-olioita käytetään säilyttämään ja kuljettamaan tietoa käyttöliittymässä ja MessageHandlerissa

src/ui 
 - sisältää käyttöliittymätiedostot ui_mainwindow.py ja ui_managementwindow.py

src/repositories
 - sisältää tiedoston db_messages.py, jonka luokka MessageDB alustaa tietokannan ja lähettää sinne tietokantakyselyt
 - tiedosto db_example_messages.py sisältää esimerkkiviestien sisällöt, joiden avulla voidaan luoda esimerkkitietokanta silloin, kun tietokantaa ei ole tallennettuna

src/tests
 - sisältää ohjelman automaattiseen testaamiseen käytettävät tiedostot




```mermaid
 classDiagram
    
      class Message{
          message_id
          text 
      }
      class MessageHandler{
          database
          group_name_list()
          all_messages_grouped()
          all_message_texts_grouped()
          messages_by_group()
          rename_group()
          delete_message()
          update_message()
          add_new_message()
      }
      class MessageDB {
          database-file
          initialize_db()
          create_example_groups()
          create_example_messages()
          get_groups()
          all_messages()
          read_messages_from_group()
          insert_new_message()
          update_message_group_name()
          update_message_text()
          delete_message_by_id()
      }
      
      class MainWindow{
          message_handler
          management_window
          group_names
          message_texts
          gui functions ()
          update_combobox_groups()
          update_combobox_contents()
      }
      
      class ManagementWindow{
          message_handler
          group_names
          messages 
          update_combobox_groups_func
          update_combobox_contents_func
          gui functions ()
      }
      
      MainWindow "1" -- "1" ManagementWindow
      MessageHandler "1" -- "1" MainWindow
      MessageHandler "1" -- "1" ManagementWindow
      ManagementWindow "1" -- "*" Message
      MessageHandler "1" -- "1" MessageDB
      
      
```
