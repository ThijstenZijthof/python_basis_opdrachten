# Opdracht 3 tekstfuncties
# Naam student: Thijs ten Zijthof
# Groep:IT2A

# Hier komt je code...
# Functie om y te berekenen volgens de gegeven formule
def bereken_y(x):
    return (4 * (x ** 3)) - (2 * (x ** 2)) - 1

# Testcases met verschillende waarden voor x
for x in [1, 2, 0]:
    print(f"De uitkomst is: {bereken_y(x)}")

