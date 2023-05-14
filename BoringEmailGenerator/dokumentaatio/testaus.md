# Testausdokumentti
Ohjelmaa on testattu automatisoidusti unittestilla, ja manuaalisesti sekä Windowsilla että Cubbli Linuxilla. Käyttöliittymää on testattu vain manuaalisesti.

## Yksikkö- ja integraatiotestaus

### Sovelluslogiikka
`MessageHandler`-luokka toimii linkkinä tietokantaluokka MessageDB:n ja käyttöliittymän välillä. Se käsittelee tietokannasta tulevan datan käyttöliittymän tarvitsemaan muotoon, ja välittää käyttöliittymän pyynnöt MessageDB:lle.
MessageHandler-luokkaa testataan [TestMessageHandler](https://github.com/SaijaGit/ot-harjoitustyo/blob/main/BoringEmailGenerator/src/tests/test_message_handler.py)-testiluokalla.

Luokka `MessageTranslator` hoitaa viestin kääntämisen googletrans-kirjaston avulla. Sitä testataan [TestMessageTranslator](https://github.com/SaijaGit/ot-harjoitustyo/blob/main/BoringEmailGenerator/src/tests/test_message_translator.py)-testiluokalla. Sen testaaminen on hieman haastavaa, sillä luokan toiminta riippuu täysin googletrans-kirjaston tarjoamasta Googlen verkossa toimivasta käännöspalvelusta, jonka ilmaisversio toimii välillä aika epäluotettavasti. Tämän takia testifunktiot yrittävät hakea käännöstä useita kertoja, mikä voi hidastaa testin suoritusta. `MessageTranslator`-luokka ilmoittaa epäonnistumisesta viesti-ikkunalla, jossa pyydetään käyttäjältä ohjeita haluaako tämä yrittää käännöstä uudelleen. Epäonnistuneen käännösyrityksen aiheuttamaa poikkeusta ja käyttäjän viesti-ikkunassa tekemiä valintoja simuloidaan testeissä unittest.mock-moduulin avulla.

Luokka `MessageChecker` tarkastaa, sisältääkö kopioitava viesti kenttiä, jotka voivat merkitä pakollista puuttuvaa dataa. Sitä testataan [TestMessageChecker](https://github.com/SaijaGit/ot-harjoitustyo/blob/main/BoringEmailGenerator/src/tests/test_message_checker.py)-testiluokalla. Myös `MessageChecker` kysyy käyttäjältä, miten tämä haluaa edetä, jos viestistä näyttäisi puuttuvan pakollista tietoa. Käyttäjän valintojen simuloimiseen käytetään myös näissä testeissä unittest.mock-moduulia.

### Repositorio-luokat

Tietokantaa käsittelevä luokka `MessageDB` hoitaa viestinnän tietokannan kanssa ja varmistaa, että ohjelman käynnistyessä tarjolla on käyttökelpoinen tietokanta. Esimerkkitietokannan alustamiseen käytetään apuna myös moduulia `db_example_messages.py`.
MessageDB-luokkaa ja `db_example_messages.py`-tiedostoa testataan [TestMessageDB](https://github.com/SaijaGit/ot-harjoitustyo/blob/main/BoringEmailGenerator/src/tests/test_db_messages.py)-testiluokalla. 
 

### Testauskattavuus

Sovelluksen testauksen haarautumakattavuus on 90%. Automaattisissa testeissä ei ole mukana käyttöliittymä eikä index.py. 

![](./kuvat/Screenshot%202023-05-11%20at%2012-56-03%20Coverage%20report.png)

## Järjestelmätestaus

Sovelluksen järjestelmätestaus on suoritettu manuaalisesti Windows 10- ja Helsingin yliopiston Cubbli linux -ympäristöissä. Ohjelma toimii samalla tavalla molemmissa ympäristöissä, mutta käyttöliittymässä on pieniä eroavaisuuksia.

### Asennus ja konfigurointi

Sovellus on nodettu ja sen testit on ajettu [käyttöohjeen](./kayttoohje.md) kuvaamalla tavalla sekä Windows 10- että Linux-ympäristöissä. Tietokantatiedostojen nimeäminen on testattu määrittelemällä erilaisia tiedostonimiä _.env_-tiedoston avulla.

Sovellusta on testattu sekä tilanteissa, joissa tietokantatiedosto on ollut olemassa, sekä ilman valmista tiedostoa.

### Toiminnallisuudet

Kaikki [määrittelydokumentin](./vaatimusmaarittely.md#perusversion-tarjoama-toiminnallisuus) ja käyttöohjeen listaamat toiminnallisuudet on testattu. Kaikkien toiminnallisuuksien yhteydessä on yritetty tehdä ohjelmalle myös epäloogisia pyyntöjä, kuten klikkailla nappeja toistuvasti, tyhjentää tietokantaa ja syöttää pitkiä tekstejä.

## Sovellukseen jääneet laatuongelmat

Sovellus näyttää hieman erilaiselta Windows- ja Linux-ympäristöissä. Muokkausikkunan selaus hiiren rullalla ei toimi Linuxissa, mutta ikkunan reunan vierityspalkki toimii. Lisäksi Linuxissa pudotusvalikkoja selatessa hiirellä kulloinkin osoitettavan vaihtoehdon tausta ei värjäydy, kuten Windowsissa. Osoitettavan vaihtoehdon valinta kuitenkin toimii oikein.
