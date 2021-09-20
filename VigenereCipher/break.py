#!/usr/bin/python3

# Breaking the Vigenere Cipher >>ASSUMINE WE KNOW PERIOD IS 3<<<!!!!

# === 1. BEGIN SETUP ===

alphabet = 'abcdefghijklmnopqrstuvwxyz'

# Character frequencies
character_frequencies = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015,
                        0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749,
                        0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758,
                        0.00978, 0.02360, 0.00150, 0.01974, 0.00074]
                        
period = 3

#cipher_text = 'opkwweciyopkwirgitypkdavgiedvmjcznqjzenzzkopkrmgopkmqyqmxtvoxm' # Want to produce 'theboyhastheballandheisplayingoutsidewheretheweatherisverynice'
#cipher_text = 'opkrmgopkmwaoaoymzjlgtqyqmxtvoxm' # Want to produce 'theweatheroutsidetodayisverynice'
cipher_text = 'vzqvvyvanvavvzzdkokizzloinupzztaosctdbkyazvbknxxzaoymtoqggmrzkzdwtnaoikkopknbgomcvagyuoobkyqtowzcmaiqui' # Want to produce 'arkansashasparticipatedinfourtysixunitedstatespresidentialelectionssincethestatewasadmittedintotheunion'

bin_1 = [] # contains all letters in ciphertext shifted by the first letter of the key
bin_2 = [] # contains all letters in ciphertext shifted by the second letter of the key
bin_3 = [] # contains all letters in ciphertext shifted by the third letter of the key

key = ''
                        
# === 2. BEGIN GROUPING OF LETTERS ===

for index,letter in enumerate(cipher_text):
    if index % period == 0:
        bin_1 += letter
    if index % period == 1:
        bin_2 += letter
    if index % period == 2:
        bin_3 += letter

# === END GROUPING OF LETTERS ===

# === 3. BEGIN FREQUENCY ANALYSIS ===

def frequency_analysis(sequence):
    """
    frequency_analysis Utilizes Chi Squared statistical analysis to determine key character
    
    This function performs a frequency analysis on the incoming sequence of characters (presumably cipher text)
    and returns the letter for that part of the key. The Chi Squared Statistic is leveraged to to measure how 
    similar the probablity distributions of the cipher text and english letter distribution is

    :sequence: String of characters that were shifted by the same key
    """
    alphabet_length = len(alphabet)
    chi_squared_columns = [0] * alphabet_length

    for index in range(alphabet_length):

        chi_squared_sum = 0.0

        #sequence_offset = [(((seq_ascii[j]-97-i)% alphabet_length )+97) for j in range(len(seq_ascii))]
        sequence_offset = [chr(((ord(sequence[j]) - 97 - index) % alphabet_length )+97) for j in range(len(sequence))]
        cipher_table = [0] * alphabet_length
        
        # find the sum of each each letter in the sequence_offset (in ascii)
        for letter in sequence_offset:
            cipher_table[ord(letter) - ord('a')] += 1
        
        # divide the array by the length of the sequence to get the frequency percentages
        for j in range(alphabet_length):
            cipher_table[j] *= ( 1.0 / float(len(sequence)))

        # compare to the cipher letter frequencies to the english letter frequencies
        for j in range(alphabet_length):
            # apply chi squared distribution 
            chi_squared_sum+=((cipher_table[j] - float(character_frequencies[j]))**2)/float(character_frequencies[j])

        # add to overall table of chi squareds
        chi_squared_columns[index] = chi_squared_sum

    # find the smallest chi-squared statistic (smallest difference between sequence distribution and 
    # english distribution allows us to determine which letter is which)
    smallest_diff = min(chi_squared_columns)
    shift = chi_squared_columns.index(smallest_diff)

    # return the letter of the key that it needs to be shifted by
    return chr(shift+97)

# === END FREQUENCY ANALYSIS ===

# === BEGIN FREQUNECY ANALYSIS OF EACH BIN ===

print("-------------------")
print("Breaking the Vigenere Cipher")
print("-------------------")

print("Cipher text: " + cipher_text)

key += frequency_analysis(bin_1)
key += frequency_analysis(bin_2)
key += frequency_analysis(bin_3)

print("The key used to encrypt the plain text is: " + key)

# === Resources ===
# https://www.youtube.com/watch?v=QgHnr8-h0xI @ 12:54
# https://www.youtube.com/watch?v=LaWp_Kq0cKs @ 5:42
