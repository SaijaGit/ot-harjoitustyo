# Boring Email Generator

Sovellus on harjoitustyö Helsingin yliopiston kurssille Ohjelmistotekniikka, kevät 2023.

Sovelluksen tarkoitus on auttaa käyttäjää luomaan yksinkertaisia sähköpostiviestejä nopeasti ja helposti.
Monet ihmiset joutuvat kirjoittamaan työssään tylsiä rutiiniviestejä, joissa on yhä uudelleen toistuvaa sisältöä, kuten esimerkiksi kaupallisia ehtoja. 
Tämän sovelluksen avulla käyttäjä voi tallentaa usein käyttämänsä viestitekstit sovellukseen helposti löydettäviksi viestipohjiksi, ja koota ja kopioida niistä uusia viestejä sähköpostiohjelmaan liitettäväksi.

## Dokumentaatio
- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](./dokumentaatio/tuntikirjanpito.md)
- [Testikattavuusraportti 2.5.2023](./dokumentaatio/testaus.md)
- [Changelog](./dokumentaatio/Changelog.md)
- [Arkkitehtuurikuvaus](./dokumentaatio/arkkitehtuuri.md)

## Docstring-kommentit
Docstring-kommentit lisätty luokille message_checker.py ja message_translator.py
- [message_checker.py](./src/message_checker.py)
- [message_translator.py](./src/message_translator.py)

## Release
- [katselmointi](https://github.com/SaijaGit/ot-harjoitustyo/releases/tag/katselmointi)

## Ohjelman asennus ja ajaminen Poetryllä

- Asenna riippuvuudet komennolla:

```bash
poetry install
```

- Alusta ohjelman suoritus komennolla:

```bash
poetry run invoke build
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

Raportti generoituu _htmlcov_-hakemistoon.

### Pylint

Suorita tiedoston [.pylintrc](./.pylintrc) määrittelemät tarkistukset komennolla:

```bash
poetry run invoke lint
```
