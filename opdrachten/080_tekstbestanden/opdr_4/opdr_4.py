# Opdracht 4 Tekst opslaan
# Naam student:
# Groep:


# Party enquete
# Vragenlijst
vragen = [
    "Wat is je voornaam?", 
    "Wat is je achternaam?", 
    "Wat neem je mee aan drank?", 
    "Wat neem je mee om te eten?"
]

# Functie om de gegevens van een feestganger op te slaan
def bevragen_feestganger():
    feestganger = {}
    print("Beantwoord de volgende vragen:")
    
    # Stel de vragen en sla de antwoorden op in de dictionary
    for i, vraag in enumerate(vragen, 1):
        antwoord = input(f"{i}. {vraag}  \n")
        if i == 1:
            feestganger["voornaam"] = antwoord
        elif i == 2:
            feestganger["achternaam"] = antwoord
        elif i == 3:
            feestganger["drank"] = antwoord
        elif i == 4:
            feestganger["eten"] = antwoord
    
    return feestganger

# Vraag de feestganger om gegevens in te voeren
feestganger_gegevens = bevragen_feestganger()

# Opslaan van de gegevens in een tekstbestand
with open("feestganger_gegevens.txt", "a") as bestand:
    bestand.write("----\n")
    for key, value in feestganger_gegevens.items():
        bestand.write(f"{key}: {value}\n")
    bestand.write("\n")

# Bevestiging aan de gebruiker
print("\nBedankt voor het invullen!") 
print("See you at the party.")
