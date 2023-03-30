
# Ohjelmistotekniikka, kevät 2023 - Tehtävät
## Viikko 3
### Tehtävä 2: Laajennettu Monopoli

Laajennetaan edellisen tehtävän luokkakaaviota tuomalla esiin seuraavat asiat:

- Ruutuja on useampaa eri tyyppiä: Aloitusruutu, Vankila, Sattuma ja yhteismaa, Asemat ja laitokset, Normaalit kadut (joihin liittyy nimi)
- Monopolipelin täytyy tuntea sekä aloitusruudun että vankilan sijainti.
- Jokaiseen ruutuun liittyy jokin toiminto.
- Sattuma- ja yhteismaaruutuihin liittyy kortteja, joihin kuhunkin liittyy joku toiminto.
- Toimintoja on useanlaisia. Ei ole vielä tarvetta tarkentaa toiminnon laatua.
- Normaaleille kaduille voi rakentaa korkeintaan 4 taloa tai yhden hotellin. Kadun voi omistaa joku pelaajista. Pelaajilla on rahaa.

Luokkakkaavio:

```mermaid
classDiagram
    Monopolipeli "1" -- "1" Pelilauta
    Monopolipeli "1" -- "2..8" Pelaaja
    Monopolipeli "1" -- "2" Noppa

    class Monopolipeli{
    }
    class Noppa{
    }
    class Pelaaja{
    }

    Raha "*" -- "1" Pelaaja
    class Raha{
    }

    Pelinappula "1" -- "1" Pelaaja
    Pelinappula "0..8" -- "1" Ruutu
    class Pelinappula{
        Ruutu
    }

    Ruutu "40" -- "1" Pelilauta 
    Ruutu "1" --> "1" Ruutu
    Toiminto "1" --> "*" Ruutu
    class Ruutu{
        seuraava
    }

    class Toiminto{
        laatu
    }

    Aloitusruutu --|> Ruutu
    Vankila --|> Ruutu
    Sattuma ja yhteismaa --|> Ruutu
    Asemat ja laitokset --|> Ruutu
    Normaalit kadut --|> Ruutu

    Aloitusruutu "1" ..> "1" Monopolipeli
    Vankila "1" ..> "1" Monopolipeli

    class Aloitusruutu{
    }
    class Vankila{
    }
    class Sattuma ja yhteismaa{
    }
    class Asemat ja laitokset{
    }
    class Normaalit kadut{
        nimi
    }

    Kortti "*" -- "*" Sattuma ja yhteismaa 
    Kortti "1" --> "*" Ruutu
    class Kortti{
    }

    Talo "0..4" -- "1" Normaalit kadut
    Hotelli "0..1" -- "1" Normaalit kadut
    Normaalit kadut "*" -- "0..1" Pelaaja
    class Talo{
    } 
    class Hotelli{
    }



```
