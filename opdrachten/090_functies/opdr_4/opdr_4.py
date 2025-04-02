# Opdracht 1 functies
# Naam student:
# Groep:


def volledige_naam(lijst_met_namen):
    for naam in lijst_met_namen:
        # Maak de volledige naam door voornaam, eventueel tussenvoegsel en achternaam te combineren
        volledige_naam = f"{naam['voornaam']} {naam['tussenvoegsel']} {naam['achternaam']}".strip()
        print(volledige_naam)

# Voorbeeld van een lijst met namen
namen = [
    {"voornaam": "Willem", "tussenvoegsel": "van", "achternaam": "Dijk"},
    {"voornaam": "Klaas", "tussenvoegsel": "", "achternaam": "Wopstra"},
    {"voornaam": "Miep", "tussenvoegsel": "van der", "achternaam": "Plas"},
    {"voornaam": "Carla", "tussenvoegsel": "", "achternaam": "Hoogvliet"},
]

# Aanroepen van de functie
volledige_naam(namen)
