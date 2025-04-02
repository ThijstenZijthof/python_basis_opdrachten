# Opdracht 2 berekeningen
# Naam student:
# Groep:

# Hier komt je code...

# Maak een lijst met de gasten
gasten = []

# Voeg jezelf en de andere gasten toe aan de lijst
gasten.append("Jij")
gasten.append("Paul")
gasten.append("Kees")
gasten.append("Marie")
gasten.append("Hilda")

# Print de originele lijst
print(gasten)  # Output: ["Jij", "Paul", "Kees", "Marie", "Hilda"]

# Verwijder Marie uit de lijst
gasten.remove("Marie")

# Print de lijst na het verwijderen van Marie
print(gasten)  # Output: ["Jij", "Paul", "Kees", "Hilda"]

# Voeg George toe naast Kees (direct na Kees' positie)
kees_index = gasten.index("Kees")  # Vind de index van Kees
gasten.insert(kees_index + 1, "George")  # Voeg George in op de juiste plek

# Print de uiteindelijke lijst
print(gasten)  # Output: ["Jij", "Paul", "Kees", "George", "Hilda"]
