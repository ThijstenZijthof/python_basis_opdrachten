# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

# Vraag de gebruiker om een lijst met minimaal 5 objecten, gescheiden door komma's
user_input = input("Zwole", "Zaanstad", "Haarlem", "Dronten", "Amsterdam")

# Converteer de invoer naar een lijst door te splitsen op ", " (let op de spatie na de komma)
items = user_input.split(", ")

# Sorteer de lijst in omgekeerde alfabetische volgorde
items.sort(reverse=True)

# Print de gesorteerde lijst
print(items)