# Opdracht 1 functies
# Naam student:
# Groep:

# importeer de module csv...
# my_modules/csv.py

# my_modules/csv.py

import csv

# Functie om gegevens naar een CSV-bestand te schrijven
def schrijf_naar_csv(bestandsnaam, data):
    """Schrijf de gegeven data naar een CSV-bestand."""
    with open(bestandsnaam, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
        print(f"Data succesvol geschreven naar {bestandsnaam}")
