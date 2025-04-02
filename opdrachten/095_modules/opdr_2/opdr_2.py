# Opdracht 1 modules
# Naam student:
# Groep:

# import .....
# for line in open("test.csv", 'rt'):
#   jouw code komt hier!

personen = [
    {"voornaam": "Jan", "tussenvoegsel": "Van Der", "achternaam": "Vliet", "plaats": "Amsterdam"},
    {"voornaam": "Piet", "tussenvoegsel": "", "achternaam": "De Vries", "plaats": "Rotterdam"},
    {"voornaam": "Griet", "tussenvoegsel": "Van Der", "achternaam": "Pol", "plaats": "Utrecht"},
    {"voornaam": "Jan", "tussenvoegsel": "Jaap", "achternaam": "Siewers", "plaats": "Groningen"},
    {"voornaam": "Pieter", "tussenvoegsel": "", "achternaam": "Jansen", "plaats": "Den Haag"},
]

def filter(persoon_lijst, filterveld, filter):
    """Filter de lijst van personen op basis van een veld en een filter."""
    
    # Resultatenlijst voor personen die voldoen aan de filtercriteria
    gefilterde_personen = []
    
    # Loop door de lijst van personen
    for persoon in persoon_lijst:
        # Controleer of het filterveld bestaat en of het filter overeenkomt met de beginletters van het veld
        if filterveld in persoon and persoon[filterveld].lower().startswith(filter.lower()):
            gefilterde_personen.append(persoon)
    
    # Print de gefilterde personen
    for persoon in gefilterde_personen:
        # Print de naam van de persoon
        volledige_naam = f"{persoon['voornaam']} {persoon['tussenvoegsel']} {persoon['achternaam']}".strip()
        print(volledige_naam)

# Voorbeeld aanroepen van de filterfunctie:
filter(personen, "voornaam", "ja")  # Filter op voornaam die begint met "ja"
filter(personen, "plaats", "d")  # Filter op plaats die begint met "d"
