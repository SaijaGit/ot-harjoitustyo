# Boring Email Generator

Sovellus on harjoitustyö Helsingin yliopiston kurssille Ohjelmistotekniikka, kevät 2023.

Sovelluksen tarkoitus on auttaa käyttäjää luomaan yksinkertaisia sähköpostiviestejä nopeasti ja helposti.

## Pikaohje


### Ohjelman asennus ja ajaminen Poetryllä

- Asenna riippuvuudet komennolla:

```bash
poetry install
```

- Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

### Komentorivitoiminnot


Käynnistä ohjelma komennolla:

```bash
poetry run invoke start
```

Käynnistä testit komennolla:

```bash
poetry run invoke test
```


Generoi testikattavuusraportti komennolla:

```bash
poetry run invoke coverage-report
```


Suorita tiedoston [.pylintrc](./.pylintrc) määrittelemät tarkistukset komennolla:

```bash
poetry run invoke lint
```
