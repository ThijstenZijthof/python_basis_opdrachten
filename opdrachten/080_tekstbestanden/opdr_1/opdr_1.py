# Opdracht 1 while-loops
# Naam student:
# Groep:

# Jouw code komt hier

# Vragen voor de enquête
vragen = [
    "Wat vind je van de huidige regering?",
    "Wat vind je van de Python-lessen tot nu toe?",
    "Wat vind jij de mooiste stad van Nederland?"
]

# Open een tekstbestand in schrijfmodus
with open("enquete_resultaten.txt", "w") as bestand:
    # Loop door de lijst van vragen en vraag de gebruiker om een antwoord
    for vraag in vragen:
        antwoord = input(f"{vraag} ")
        bestand.write(f"{vraag}\n{antwoord}\n\n")

print("De antwoorden zijn opgeslagen in 'enquete_resultaten.txt'.")
