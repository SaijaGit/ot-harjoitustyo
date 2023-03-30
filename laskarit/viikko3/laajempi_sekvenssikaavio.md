
# Ohjelmistotekniikka, kevät 2023 - Tehtävät
## Viikko 3
### Tehtävä 3: Sekvenssikaavio

Sekvenssikaavio kuvitteellisen HSL-matkakorttien hallintaan käytettävän koodin main-funktion toiminnallisuudelle.



Sekvenssikaavio:

```mermaid
sequenceDiagram
    participant main
    participant Kioski
    participant Matkakortti
    participant Lataajalaite
    participant Lukijalaite
    participant HKLLaitehallinto

    main ->> HKLLaitehallinto: Luodaan uusi HKLLaitehallinto-olio
    main ->> Lataajalaite: Luodaan uusi Lataajalaite-olio (rautatietori)
    main ->> Lukijalaite: Luodaan uusi Lukijalaite-olio (ratikka6)
    main ->> Lukijalaite: Luodaan uusi Lukijalaite-olio (bussi244)
    main ->> HKLLaitehallinto: lisaa_lataaja(rautatietori)
    main ->> HKLLaitehallinto: lisaa_lukija(ratikka6)
    main ->> HKLLaitehallinto: lisaa_lukija(bussi244)

    main ->> Kioski: Luodaan uusi Kioski-olio
    main ->> Kioski: osta_matkakortti("Kalle")
    Kioski ->> Matkakortti: Luodaan uusi Matkakortti-olio
    main ->> Lataajalaite: lataa_arvoa(kallen_kortti, 3)
    Lataajalaite ->> Matkakortti: kasvata_arvoa(3)

    main ->> Lukijalaite: osta_lippu(kallen_kortti, 0)
    Lukijalaite ->> Matkakortti: vahenna_arvoa(1.5)
    Lukijalaite ->> main: return True
    main ->> Lukijalaite: osta_lippu(kallen_kortti, 2)
    Lukijalaite ->> main: return False

```
