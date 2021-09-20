#!/usr/bin/python3

# Breaking the Vigenere Cipher >>ASSUMINE WE KNOW PERIOD IS 3<<<!!!!

# === 1. BEGIN SETUP ===

alphabet = 'abcdefghijklmnopqrstuvwxyz'
period = 3
bin_1 = [] # contains all letters shifted by first letter
bin_2 = [] # contains all letters shifted by second letter
bin_3 = [] # contains all letters shifted by third letter
cipher_text = 'opkwweciyopkwirgitypkdavgiedvmjcznqjzenzzkopkrmgopkmqyqmxtvoxm' # Want to produce 'theboyhastheballandheisplayingoutsidewheretheweatherisverynice'
plain_text = ''

# Character frequencies
character_frequencies = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015,
                        0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749,
                        0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758,
                        0.00978, 0.02360, 0.00150, 0.01974, 0.00074]
                        
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
print(bin_1)
print(bin_2)
print(bin_3)

def freq_analysis(sequence):
	all_chi_squareds = [0] * 26

	for i in range(26):

		chi_squared_sum = 0.0

		#sequence_offset = [(((seq_ascii[j]-97-i)%26)+97) for j in range(len(seq_ascii))]
		sequence_offset = [chr(((ord(sequence[j])-97-i)%26)+97) for j in range(len(sequence))]
		v = [0] * 26
		# count the numbers of each letter in the sequence_offset already in ascii
		for l in sequence_offset:
			v[ord(l) - ord('a')] += 1
		# divide the array by the length of the sequence to get the frequency percentages
		for j in range(26):
			v[j] *= (1.0/float(len(sequence)))

		# now you can compare to the english frequencies
		for j in range(26):
			chi_squared_sum+=((v[j] - float(character_frequencies[j]))**2)/float(character_frequencies[j])

		# add it to the big table of chi squareds
		all_chi_squareds[i] = chi_squared_sum

	# return the letter of the key that it needs to be shifted by
	# this is found by the smallest chi-squared statistic (smallest different between sequence distribution and 
	# english distribution)
	shift = all_chi_squareds.index(min(all_chi_squareds))

	# return the letter
	return chr(shift+97)

print(freq_analysis(bin_1))
print(freq_analysis(bin_2))
print(freq_analysis(bin_3))

# https://www.youtube.com/watch?v=QgHnr8-h0xI @ 12:54
# https://www.youtube.com/watch?v=LaWp_Kq0cKs @ 5:42
