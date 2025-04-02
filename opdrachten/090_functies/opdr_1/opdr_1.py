# Opdracht 1 functies
# Naam student:
# Groep:


# Functie die tekst naar een bestand schrijft
def write_to_file(bestand_naam, tekst):
    # Open het bestand in append-modus ('a'), zodat tekst wordt toegevoegd
    with open(bestand_naam, 'a') as bestand:
        bestand.write(tekst + '\n')  # Voeg de tekst toe en een nieuwe regel

# Voorbeeld van het gebruik van de functie
my_tekst = "Schrijf dit maar even in een bestandje"
my_file = "test.txt"
write_to_file(my_file, my_tekst)

