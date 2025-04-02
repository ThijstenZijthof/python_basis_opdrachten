# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

# Hier start de for-loop

# Beginlijst pizza's
pizzas = ['margharita', 'calzone', 'verdi', 'olivio', 'quattro stagioni']

# Sorteer de lijst op alfabet
pizzas.sort()
print(pizzas)  # Output: ['calzone', 'margharita', 'olivio', 'quattro stagioni', 'verdi']

# Voeg een pizza toe naar eigen smaak
pizzas.append('yo-favorito')
print(pizzas)  # Output: ['calzone', 'margharita', 'olivio', 'quattro stagioni', 'verdi', 'yo-favorito']

# Verwijder de pizza die je het minst lekker vindt
pizzas.remove('olivio')
print(pizzas)  # Output: ['calzone', 'margharita', 'quattro stagioni', 'verdi', 'yo-favorito']

# Print de eerste 3 pizza's
print(pizzas[:3])  # Output: ['calzone', 'margharita', 'quattro stagioni']

# Print alleen de middelste pizza uit de lijst
print([pizzas[len(pizzas) // 2]])  # Output: ['quattro stagioni']

# Print de laatste 3 pizza's
print(pizzas[-3:])  # Output: ['quattro stagioni', 'verdi', 'yo-favorito']

