# Opdracht 1 input function
# Naam student:
# Groep:

# Hier komt je code, maak gebruik van de input functie om de lengte van de rechthoekzijden van de driehoek op te vragen.

import math  # Importeer de math-module voor de wortelfunctie

# Vraag de gebruiker om invoer voor de twee zijden van de rechthoekige driehoek
a = float(input("Geef de lengte van de eerste zijde\n"))
b = float(input("Geef de lengte van de tweede zijde\n"))

# Bereken de schuine zijde (c) met de stelling van Pythagoras: c² = a² + b²
c = math.sqrt(a**2 + b**2)

# Print het resultaat, afgerond op 5 decimalen
print(f"\nDe lengte van de schuine zijde is: {round(c, 5)}")
