
# Ohjelmistotekniikka, kevät 2023 - Tehtävät
## Viikko 3
### Tehtävä 4: Laajempi sekvenssikaavio

Sekvenssikaavio kuvitteellisen HSL-matkakorttien hallintaan käytettävän koodin main-funktion toiminnallisuudelle.



Sekvenssikaavio:


```mermaid
sequenceDiagram
    participant main
    
    participant HKLLaitehallinto
    participant Lataajalaite
    participant Lukijalaite


    main ->> HKLLaitehallinto: Luodaan uusi HKLLaitehallinto-olio
    main ->> Lataajalaite: Luodaan uusi Lataajalaite-olio (rautatietori)
    main ->> Lukijalaite: Luodaan uusi Lukijalaite-olio (ratikka6)
    main ->> Lukijalaite: Luodaan uusi Lukijalaite-olio (bussi244)
    main ->> HKLLaitehallinto: lisaa_lataaja(rautatietori)
    main ->> HKLLaitehallinto: lisaa_lukija(ratikka6)
    main ->> HKLLaitehallinto: lisaa_lukija(bussi244)
    
    participant Kioski
    participant Matkakortti
    
    main ->> Kioski: Luodaan uusi Kioski-olio
    main ->> Kioski: osta_matkakortti("Kalle")
    Kioski ->> Matkakortti: Luodaan uusi Matkakortti-olio
    Kioski ->> main: return uusi_kortti
    
    main ->> Lataajalaite: lataa_arvoa(kallen_kortti, 3)
    Lataajalaite ->> Matkakortti: kasvata_arvoa(3)

    main ->> Lukijalaite: osta_lippu(kallen_kortti, 0)
    Lukijalaite ->> Matkakortti: vahenna_arvoa(1.5)
    Lukijalaite ->> main: return True
    main ->> Lukijalaite: osta_lippu(kallen_kortti, 2)
    Lukijalaite ->> main: return False

```
