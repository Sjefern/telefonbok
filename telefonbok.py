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