# Boring Email Generator

Sovellus on harjoitustyö Helsingin yliopiston kurssille Ohjelmistotekniikka, kevät 2023.

Sovelluksen tarkoitus on auttaa käyttäjää luomaan yksinkertaisia sähköpostiviestejä nopeasti ja helposti.
Monet ihmiset joutuvat kirjoittamaan työssään tylsiä rutiiniviestejä, joissa on yhä uudelleen toistuvaa sisältöä, kuten esimerkiksi kaupallisia ehtoja. 
Tämän sovelluksen avulla käyttäjä voi tallentaa usein käyttämänsä viestitekstit sovellukseen helposti löydettäviksi viestipohjiksi, ja koota ja kopioida niistä uusia viestejä sähköpostiohjelmaan liitettäväksi.

## Käyttöympäristö ja Python-versio
Ohjelma on testattu käyttäen Windows 10 -tietokonetta ja Pytho-versiota 3.11 sekä Linux-konetta ja Python-versiota 3.10. On mahdollista, että se ei toimi samalla tavalla muissa järjestelmissä ja varsinkaan vanhemmilla Python-versioilla.

## Dokumentaatio
- [Käyttöohje](./BoringEmailGenerator/dokumentaatio/kayttoohje.md)
- [Vaatimusmäärittely](./BoringEmailGenerator/dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus](./BoringEmailGenerator/dokumentaatio/arkkitehtuuri.md)
- [Testausdokumentti](./BoringEmailGenerator/dokumentaatio/testaus.md)
- [Työaikakirjanpito](./BoringEmailGenerator/dokumentaatio/tuntikirjanpito.md)
- [Changelog](./BoringEmailGenerator/dokumentaatio/Changelog.md)


## Ohjelman asennus ja ajaminen Poetryllä

- Asenna riippuvuudet komennolla:

```bash
poetry install
```

- Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Käynnistä ohjelma komennolla:

```bash
poetry run invoke start
```

### Testaus

Käynnistä testit komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Generoi testikattavuusraportti komennolla:

```bash
poetry run invoke coverage-report
```

Komento generoi testituloksista raportin [index.htm](./BoringEmailGenerator/dokumentaatio/kuvat/Screenshot%202023-05-11%20at%2012-56-03%20Coverage%20report.png) _htmlcov_-hakemistoon.

### Pylint

Suorita tiedoston [.pylintrc](./BoringEmailGenerator/.pylintrc) määrittelemät tarkistukset komennolla:

```bash
poetry run invoke lint
```
