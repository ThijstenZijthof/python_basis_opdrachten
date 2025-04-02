# Opdracht 1 functies
# Naam student:
# Groep:


import math  # Importeren van de math module voor pi

# Functie om het volume van een kubus te berekenen
def kubus_vol(zijde):
    volume = zijde ** 3  # Het volume van een kubus is zijde^3
    return volume

# Functie om het volume van een bol te berekenen
def bol_vol(radius):
    volume = (4/3) * math.pi * (radius ** 3)  # Het volume van een bol is (4/3) * pi * r^3
    return volume

# Voorbeeld van het gebruik van de functies
kubus_resultaat = kubus_vol(5)  # Volume van een kubus met zijde 5
bol_resultaat = bol_vol(4)  # Volume van een bol met radius 4

# Print de resultaten
print(f"De inhoud van deze kubus is: {kubus_resultaat}")
print(f"De inhoud van deze bol is: {bol_resultaat}")
