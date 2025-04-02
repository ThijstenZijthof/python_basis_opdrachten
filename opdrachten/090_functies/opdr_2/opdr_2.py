# Opdracht 1 functies
# Naam student:
# Groep:


# Functie om kilometers naar miles om te rekenen
def kilometers_naar_miles(kilometers):
    miles = kilometers / 1.609344
    return miles

# Functie om miles naar kilometers om te rekenen
def miles_naar_kilometers(miles):
    kilometers = miles * 1.609344
    return kilometers

# Voorbeeld van het gebruik van de functies
kilometers = 1223
miles = 867

# Berekeningen
miles_result = kilometers_naar_miles(kilometers)
km_result = miles_naar_kilometers(miles)

# Print de resultaten
print(f"{kilometers} kilometers = {miles_result} miles")
print(f"{miles} miles = {km_result} kilometers")
