#!/usr/bin/python3

# === 1. BEGIN SETUP ===
alphabet = "abcdefghijklmnopqrstuvwxyz"
#plain_text = "THE BOY HAS THE BALL"
#plain_text = "THE WEATHER OUTSIDE TODAY IS VERY NICE"
plain_text = "Arkansas has participated in fourty six United States presidential elections since the state was admitted in to the Union"

key = "Vig"

plain_text = plain_text.lower()
key = key.lower()

# === END SETUP ===

# === 2. BEGIN KEY EXPANSION ===
# Expand the key in the case it is shorter than the string to be encrypted
expanded_key = key
expanded_key_length = len(expanded_key)
plain_text_length = len(plain_text)

while expanded_key_length < plain_text_length:
    expanded_key = expanded_key + key
    expanded_key_length = len(expanded_key)

decrypted_string = ""

# === END KEY EXPANSION ===

def vigenere_encrypt(plain_text):
    """
    vigenere_encrypt Encrypts a string using the Vigenere Cipher method

    :plain_text: String that a user wants encrypted
    """
    plain_text = plain_text.lower()
    key_pos = 0
    encrypted_string = ""

    # Encrypt each letter
    for letter in plain_text:
        if letter in alphabet:
            index = alphabet.find(letter) # get numerical representation of plain text letter
            key_char = expanded_key[key_pos] # get numerical representation of key letter
            key_pos += 1
            key_index = ord(key_char) - 97 # 97 to get 0 index

            # enciphered index = (plaintext index + keyword index) mod 26
            encrypted_index = (index + key_index) % 26

            encrypted_char = alphabet[encrypted_index]

            encrypted_string += encrypted_char

    return encrypted_string

def vigenere_decrypt(cipher_text):
    """
    vigenere_decrypt Decrypts a string using the Vigenere Cipher method

    :cipher_text: String that a user wants decrypted
    """
    cipher_text = cipher_text.lower()
    key_pos = 0
    decrypted_string = ""

    # Decrypt each letter
    for letter in cipher_text:
        if letter in alphabet:
            index = alphabet.find(letter) # get numerical representation of plain text letter
            key_char = expanded_key[key_pos] # get numerical representation of key letter
            key_pos += 1
            key_index = ord(key_char) - 97 # 97 to get 0 index

            # enciphered index = (encipher text index - keyword index) mod 26
            decrypted_index = (index - key_index) % 26

            decrypted_char = alphabet[decrypted_index]

            decrypted_string += decrypted_char

    return decrypted_string

# === 3. BEGIN MAIN PROGRAM ===

print("-------------------")
print("Vigenere Cipher")
print("-------------------")

print("Plain text: " + plain_text)

cipher_text = vigenere_encrypt(plain_text)
print("Encrypted text: " + cipher_text)

plain_text = vigenere_decrypt(cipher_text)
print("Decrypted text: " + plain_text + "\n")

# === END MAIN PROGRAM ===
