# Testausdokumentti
Tässä vaiheessa ohjelma sisältää pääasiassa viestien käsittelyyn, tietokantaan ja käyttöliittymään liittyvää toiminnallisuutta.
Ohjelmaa on testattu automatisoidusti unittestilla, ja käyttöliittymää on testattu manuaalisesti sekä Windowsilla että Cubbli Linuxilla.

## Yksikkö- ja integraatiotestaus

### Sovelluslogiikka ja Repositorio-luokat
`MessageHandler`-luokka toimii linkkinä tietokantaluokka MessageDB:n ja käyttöliittymän välillä. Se käsittelee tietokannasta tulevan datan käyttöliittymän tarvitsemaan muotoon, ja välittää käyttöliittymän pyynnöt MessageDB:lle.
MessageHandler-luokkaa testataan [TestMessageHandler](https://github.com/SaijaGit/ot-harjoitustyo/blob/main/BoringEmailGenerator/src/tests/test_message_handler.py)-testiluokalla.


Tietokantaa käsittelevä luokka `MessageDB` hoitaa viestinnän tietokannan kanssa ja varmistaa, että ohjelman käynnistyessä tarjolla on käyttökelpoinen tietokanta. 
MessageDB-luokkaa testataan [TestMessageDB](https://github.com/SaijaGit/ot-harjoitustyo/blob/main/BoringEmailGenerator/src/tests/test_db_messages.py)-testiluokalla. 

Luokka `MessageTranslator` hoitaa viestin kääntämisen googletrans-kirjaston avulla. Sitä testataan [TestMessageTranslator](https://github.com/SaijaGit/ot-harjoitustyo/blob/main/BoringEmailGenerator/src/tests/test_message_translator.py)-testiluokalla. Sen testaaminen kattavasti on hieman haastavaa, sillä luokan toiminta riippuu täysin googletrans-kirjaston tarjoamasta googlen verokssa toimvasta käännöspalvelusta, jonka ilmaisversio toimii aika epäluotettavasti.

### Testauskattavuus

Tällä hetkellä sovelluksen testauksen haarautumakattavuus on 89%. Automaattisissa testeissä ei ole mukana käyttöliittymä eikä index.py.

![](./kuvat/Screenshot%202023-04-25%20at%2022-44-38%20Coverage%20report.png)

