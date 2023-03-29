
# Ohjelmistotekniikka, kevät 2023 - Tehtävät
## Viikko 3
### Tehtävä 1: Monopoli

Monopolia pelataan käyttäen kahta noppaa. Pelaajia on vähintään 2 ja enintään 8. Peliä pelataan pelilaudalla joita on yksi. Pelilauta sisältää 40 ruutua. Kukin ruutu tietää, mikä on sitä seuraava ruutu pelilaudalla. Kullakin pelaajalla on yksi pelinappula. Pelinappula sijaitsee aina yhdessä ruudussa.

Alustava luokkakkaavio:

```mermaid
classDiagram
    Ruutu "40" -- Pelilauta 
    class Ruutu{
        seuraava
    }
    Noppa "2" -- "1" Pelilauta
    class Noppa{
        silmäluku
    }
    Pelaaja "2..8" -- "1" Pelilauta
    class Pelaaja{
        Pelinappula
    }

    Pelinappula "1" -- "1" Pelaaja
    Pelinappula "1" -- "1" Ruutu
    class Pelinappula{
        Ruutu
    }



```
