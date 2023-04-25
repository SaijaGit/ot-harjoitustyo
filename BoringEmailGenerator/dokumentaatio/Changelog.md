# Changelog

## Viikko 3
- Lisätty käyttöliittymän pääikkuna (luokka UI tiedostossa ui_mainwindow.py)
- Toteutettu pääikkunaan viestipohjien valinta alasvetovalikoista ja sijoittaminen tekstikenttään, sekä tekstikentän sisällön tyhjennys ja kopiointi leikepöydälle
- Lisätty MessageDB-luokka hoitamaan viestipohjien tallentamista tietokantaan ja niiden noutamista tietokannasta
- Lisätty esimerkkiviestipohjien luonti tietokantaan ohjelman käytön aloittamista ja testausta varten (db_example_messages.py)
- Testattu, että MessageDB-luokka alustaa tietokannan ja luo sinne tarvittaessa esimerkkiviestipohjat, ja että viestiryhmien nimien ja viestien lisäys, poisto ja haku tietokannasta toimii oikein.

## Viikko 4
- Lisätty käyttöliittymään toinen ikkuna ManagemetWindow, jossa voi vaihtaa viestiryhmien nimet sekä lisätä, muokata ja poistaa viestipohjia.
- Luotu uusi luokka MessageHandler toimimaan käyttöliittymän ja tietokantaa hoitavan MessageDB-luokan väliin. Sen avulla saatiin siistittyä käyttöliittymän ja MessageDB:n koodia, sillä se hoitaa tiedon muuntamisen molempien luokkien tarvitsemaan muotoon.
- Lisättiin Pylint ja korjattiin sen ilmoittamat virheet.
- Lisättiin testit MessageHandler-luokalle.

## Viikko 5
- Lisätty käännöstä varten kielivalikot ja käynnistysnappi pääikkunaan.
- Siirretty käyttöliittymän tyylimäärittelyt omaan tiedostoon ja siistitty käyttöliittymäluokkia.
- Luotu uusi luokka MessageTranslator hoitamaan viestien kääntämistä googletrans-kirjaston avulla.
- Lisättiin testit MessageTranslator-luokalle.
- Koska googletrans ei aina toimi luotettavasti, on luotu myös InfoWindow-ikkuna, jonka on tarkoitus viestiä käyttäjälle käännöksen toiminnasta. Se ei ole vielä valmis, joten on toistaiseksi kommentoitu pois.
