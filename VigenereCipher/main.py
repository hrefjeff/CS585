#!/usr/bin/python3

# Variables and Setup
alphabet = "abcdefghijklmnopqrstuvwxyz"
plain_text = "THE BOY HAS THE BALL"
key = "Vig"

plain_text = plain_text.lower()
key = key.lower()

# Expand the key in the case it is shorter than the string to be encrypted
expanded_key = key
expanded_key_length = len(expanded_key)
plain_text_length = len(plain_text)

while expanded_key_length < plain_text_length:
    expanded_key = expanded_key + key
    expanded_key_length = len(expanded_key)

decrypted_string = ""

# Enter the string that needs to be encrypted here
def vigenere_encrypt(plain_text):

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


print("-------------------")
print("Vigenere Cipher")
print("-------------------")
print("Plain text: " + plain_text)
print("Encrypted text: " + vigenere_encrypt(plain_text))
print("Decrypted text: " + decrypted_string + "\n")