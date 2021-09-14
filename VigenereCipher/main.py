#!/usr/bin/python3

# Global variables
alphabet = "abcdefghijklmnopqrstuvwxyz"
input_string = ""
key = ""
expanded_key = ""
encrypted_string = ""
decrypted_string = ""

# Enter key here
key = "Vig"
key = key.lower()

# Enter the string that needs to be encrypted here
input_string = "THE BOY HAS THE BALL"
input_string = input_string.lower()

# Expand the key in the case it is shorter than the string to be encrypted
expanded_key = key
expanded_key_length = len(expanded_key)
input_string_length = len(input_string)

while expanded_key_length < input_string_length:
    expanded_key = expanded_key + key
    expanded_key_length = len(expanded_key)