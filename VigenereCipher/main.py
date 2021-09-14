#!/usr/bin/python3

# Global variables
alphabet = "abcdefghijklmnopqrstuvwxyz"
plain_text = ""
key = ""
expanded_key = ""
encrypted_string = ""
decrypted_string = ""
i = 0

# Enter key here
key = "Vig"
key = key.lower()

# Enter the string that needs to be encrypted here
plain_text = "THE BOY HAS THE BALL"
plain_text = plain_text.lower()

# Expand the key in the case it is shorter than the string to be encrypted
expanded_key = key
expanded_key_length = len(expanded_key)
plain_text_length = len(plain_text)

while expanded_key_length < plain_text_length:
    expanded_key = expanded_key + key
    expanded_key_length = len(expanded_key)

# Encrypt each letter
for letter in plain_text:
    if letter in alphabet:
        index = alphabet.find(letter) # get numerical representation of plain text letter
        key_char = expanded_key[i] # get numerical representation of key letter
        i += 1
        key_index = ord(key_char) - 97 # 97 to get 0 index

        # enciphered index = (plaintext index + keyword index) mod 26
        encrypted_index = (index + key_index) % 26

        encrypted_char = alphabet[encrypted_index]

        encrypted_string = encrypted_string + encrypted_char


print("-------------------")
print("Vigenere Cipher")
print("-------------------")
print("Plain text: " + plain_text)
print("Encrypted text: " + encrypted_string)
print("Decrypted text: " + decrypted_string + "\n")