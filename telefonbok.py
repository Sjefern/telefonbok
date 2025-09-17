#telefon bok

# Lager en tom telefonbok liste
telefonbok = []

# Lager ordbøker med to personer og tlf nummeret
Person1 = {"navn":"Sebastian", "nummer": 1479643}
Person2 = {"navn":"Marcus", "nummer": 14767883}

# legger til begge personene til i listen ved å bruke apend
telefonbok.append(Person1)
telefonbok.append(Person2)

# lager en funskjon
def vis_alle():
    for person in telefonbok:
        print(f"navn: {person["navn"]}, nummer: {person["nummer"]}")

# vi tilkaller løkken
vis_alle() 

# vi lager en tli funksjon
def legg_til():
    input

# ber brukeren skrive inn navn og nummer
navn = input("Skriv inn navn: ")
nummer = input(" skriv inn nummmer: ")

# lager en ordbok med infoen
ny_persjon = {"navn": navn, "nummer": nummer}

# legger ordboken inn i lista telefonbok
telefonbok.append(ny_persjon)

# viser en melding om at personen ble lagt til.
print(f"{navn} ble lagt til i telefonboka.")

# lager en funksjon
def søk():
    # Ber brukeren skrive inn et navn og gjør det om til små bokstaver for enklere sammenligning
    søkenavn = input("Skriv inn navnet du vil søke etter: ").lower()
    # lager et flagg som viser om vi har funnet noen eller ikke
    funnet = False
    # går gjennom alle personer i telefonbok-listen
    for person in telefonbok:
        # sjekker om navnet til personen er likt søkenavnet
        if person["navn"].lower() == søkenavn:
            # skriver ut navn og nummer hvis det er en match
            print(f"Fant: {person['navn']} - {person['nummer']}")
            # markerer at vi har funnet en person.
            funnet = True
            # stopper løkken når en match er funnet
            break
    # sjekker om ingen ble funnet
    if not funnet:
        # skriver ut melding hvis ingen ble funnet
        print("Fant ingen med det navnet.")

