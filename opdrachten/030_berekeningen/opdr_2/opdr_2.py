# Opdracht 2 berekeningen
# Naam student: Thijs ten Zijthof
# Groep:IT2A

# Hier komt je code...

# Functie om Celsius naar Fahrenheit om te rekenen
def celsius_naar_fahrenheit(c):
    return (c * 9/5) + 32

# Functie om Fahrenheit naar Celsius om te rekenen
def fahrenheit_naar_celsius(f):
    return (f - 32) * 5/9

# Eerste set waarden
c = -12
f = 102
print(f"{c} graden Celsius is gelijk aan {celsius_naar_fahrenheit(c):.1f} graden Fahrenheit")
print(f"{f} graden Fahrenheit is gelijk aan {fahrenheit_naar_celsius(f):.1f} graden Celsius")

# Tweede set waarden
c = 62.2
f = 96
print(f"{c} graden Celsius is gelijk aan {celsius_naar_fahrenheit(c):.1f} graden Fahrenheit")
print(f"{f} graden Fahrenheit is gelijk aan {fahrenheit_naar_celsius(f):.1f} graden Celsius")
