
# Ohjelmistotekniikka, kevät 2023 - Tehtävät
## Viikko 3
### Tehtävä 1: Monopoli

Monopolia pelataan käyttäen kahta noppaa. Pelaajia on vähintään 2 ja enintään 8. Peliä pelataan pelilaudalla joita on yksi. Pelilauta sisältää 40 ruutua. Kukin ruutu tietää, mikä on sitä seuraava ruutu pelilaudalla. Kullakin pelaajalla on yksi pelinappula. Pelinappula sijaitsee aina yhdessä ruudussa.

Alustava luokkakkaavio:

```mermaid
classDiagram
    Monopolipeli "1" -- "1" Pelilauta
    Monopolipeli "1" -- "2..8" Pelaaja
    Monopolipeli "1" -- "2" Noppa

    class Monopolipeli{
        Pelilauta
        Pelaajat
        Noppa
    }

    Ruutu "40" -- "1" Pelilauta 
    class Ruutu{
        seuraava
    }

    class Noppa{
        silmäluku
    }

    class Pelaaja{
        Pelinappula
    }

    Pelinappula "1" -- "1" Pelaaja
    Pelinappula "0..8" -- "1" Ruutu
    class Pelinappula{
        Ruutu
    }



```
