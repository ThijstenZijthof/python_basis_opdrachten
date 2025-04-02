# Opdracht 3 Tekst opslaan
# Naam student:
# Groep:


def encrypt(text):
    encrypted_text = ""
    for char in text:
        # Controleer of het teken een letter is
        if char.isalpha():
            # Verschoven positie van de letter
            shift = 5
            # Kijk of de letter een kleine letter is
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            # Kijk of de letter een hoofdletter is
            elif char.isupper():
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            # Niet-lettertekens blijven ongewijzigd
            encrypted_text += char
    return encrypted_text

def decrypt(text):
    decrypted_text = ""
    for char in text:
        # Controleer of het teken een letter is
        if char.isalpha():
            # Verschoven positie van de letter
            shift = 5
            # Kijk of de letter een kleine letter is
            if char.islower():
                decrypted_text += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            # Kijk of de letter een hoofdletter is
            elif char.isupper():
                decrypted_text += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        else:
            # Niet-lettertekens blijven ongewijzigd
            decrypted_text += char
    return decrypted_text

# Vraag de gebruiker om een tekst in te voeren
tekst = input("Geef de tekst die je wilt encrypten..  ")

# Encrypt de tekst
geëncrypteerde_tekst = encrypt(tekst)
print("Geëncrypteerde tekst:")
print(geëncrypteerde_tekst)

# Decrypt de tekst (voor de controle)
degeëncrypteerde_tekst = decrypt(geëncrypteerde_tekst)
print("\nDecrypted tekst (controle):")
print(degeëncrypteerde_tekst)
