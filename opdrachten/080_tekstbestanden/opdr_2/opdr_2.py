# Opdracht 2 tekstbestanden
# Naam student:
# Groep:

import random

# Genereer een willekeurig getal tussen 1 en 100
geheim_getal = random.randint(1, 100)
aantal_pogingen = 0
geraden = False

print("Raad mijn geheime getal")

# Blijf vragen om een getal totdat de gebruiker het juiste getal heeft geraden
while not geraden:
    poging = int(input())  # Vraag de gebruiker om een getal in te voeren
    aantal_pogingen += 1
    
    if poging < geheim_getal:
        print("hoger")
    elif poging > geheim_getal:
        print("lager")
    else:
        print(f"Je hebt het getal geraden, het is {geheim_getal}!")
        print(f"Je hebt het in {aantal_pogingen} keer gedaan")
        geraden = True
