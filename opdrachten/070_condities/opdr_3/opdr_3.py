# Opdracht 3 condities
# Naam student:
# Groep:


# Hier komt je code...
# Gegeven variabelen
normale_toegangsprijs = 12.50
kortings_percentages = { "baby": 100, "kinderen": 50, "volwassenen": 0, "ouderen": 30 }
leeftijd = { "baby": (0,2), "kinderen": (3,18), "volwassenen": (19,64), "ouderen": (65,150) }

# Vraag de leeftijd van de bezoeker
age = int(input("Geef uw leeftijd in aantal jaar: "))

# Bepaal tot welke groep de bezoeker behoort
for groep, (min_leeftijd, max_leeftijd) in leeftijd.items():
    if min_leeftijd <= age <= max_leeftijd:
        groep_naam = groep
        korting_percentage = kortings_percentages[groep]
        break

# Bereken de te betalen prijs
korting = (korting_percentage / 100) * normale_toegangsprijs
prijs = normale_toegangsprijs - korting

# Toon de resultaten
print(f"U behoort tot de groep {groep_naam}")
print(f"U krijgt {korting_percentage}% korting")
print(f"U betaalt daarom {prijs:.2f}")
