
# Ohjelmistotekniikka, kevät 2023 - Tehtävät
## Viikko 3
### Tehtävä 3: Sekvenssikaavio

Sekvenssikaavio koneelle, joka koostuu bensatankista ja moottorista.

Kaaviossa on kuvattu tilanne, jossa kutsutaan (jostain koodin ulkopuolella olevasta metodista) ensin Machine-luokan konstruktoria ja sen jälkeen luodun Machine-olion metodia drive.



Sekvenssikaavio:

```mermaid
sequenceDiagram
    participant Caller
    participant Machine
    participant FuelTank
    participant Engine

    Caller ->> Machine: Luodaan uusi Machine-olio
    Machine ->> FuelTank: Luodaan uusi FuelTank-olio
    Machine ->> FuelTank: fill(40)
    Machine ->> Engine:  Luodaan uusi Engine-olio

    Caller ->> Machine: drive(self)
    Machine ->> Engine:  start()
    Engine ->> FuelTank: consume(5)


```
