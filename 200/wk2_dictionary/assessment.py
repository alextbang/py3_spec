# # The dictionary Junior shows a schedule for a junior year semester. The key is the course name and the value is the number of credits. Find the total number of credits taken this semester and assign it to the variable credits. Do not hardcode this – use dictionary accumulation!

# Junior = {'SI 206':4, 'SI 310':4, 'BL 300':3, 'TO 313':3, 'BCOM 350':1, 'MO 300':3}
# credits = 0

# for c in Junior:
#     credits = credits + Junior[c]
# print('credits--->', credits)


####################################

# Create a dictionary, freq, that displays each character in string str1 as the key and its frequency as the value.

# str1 = "peter piper picked a peck of pickled peppers"
# freq = {}

# for c in str1:
#     if c not in freq:
#         freq[c] = 0
#     freq[c] = freq[c] + 1

# print('freq-->', freq)

#####################################

#Provided is a string saved to the variable name s1. Create a dictionary named counts that contains each letter in s1 and the number of times it occurs.

# s1 = "hello"
# counts = {}

# for c in s1:
#     if c not in counts:
#         counts[c] = 0
#     counts[c] = counts[c] + 1

# print(counts)

#####################################

# Create a dictionary, freq_words, that contains each word in string str1 as the key and its frequency as the value.

# str1 = "I wish I wish with all my heart to fly with dragons in a land apart"

# freq_words = {}
# words = str1.split()
# print(words)

# for w in words:
#     if w not in freq_words:
#         freq_words[w] = 0
#     freq_words[w] = freq_words[w] + 1

# print(freq_words)

#####################################

#Create a dictionary called wrd_d from the string sent, so that the key is a word and the value is how many times you have seen that word.

# sent = "Singing in the rain and playing in the rain are two entirely different situations but both can be good"

# wrd_d = {}
# words = sent.split()
# print(words)

# for w in words:
#     if w not in wrd_d:
#         wrd_d[w] = 0
#     wrd_d[w] = wrd_d[w] + 1

# print(wrd_d)

#####################################

#Create the dictionary characters that shows each character from the string sally and its frequency. Then, find the most frequent letter based on the dictionary. Assign this letter to the variable best_char.


# sally = "sally sells sea shells by the sea shore"
# characters = {}

# # create a dictionary of characters and their frequency
# for c in sally:
#     if c not in characters:
#         characters[c] = 0
#     characters[c] = characters[c] + 1
# print('characters-->', characters)

# #turn dictionary into a list of keys
# ks = characters.keys()
# print('ks-->', ks)

# #initialize best_char
# best_char = list(ks)[0]
# print('initial best_char-->', best_char)

# for k in ks:
#     print('k-->', k)
#     if characters[k] > characters[best_char]:
#         best_char = k
        
# print(best_char)


#####################################

# Find the least frequent letter. Create the dictionary characters that shows each character from string sally and its frequency. Then, find the least frequent letter in the string and assign the letter to the variable worst_char.

# sally = "sally sells sea shells by the sea shore and by the road"
# characters = {}

# # create a dictionary of characters and their frequency
# for c in sally:
#     if c not in characters:
#         characters[c] = 0
#     characters[c] = characters[c] + 1

# print('characters--->', characters)

# #turn dictionary into a list of keys
# ks = characters.keys()
# print('ks--->', ks)

# #initialize worst_char
# worst_char = list(ks)[0]
# print('initial worst_char--->', worst_char)

# for k in ks:
#     if characters[k] < characters[worst_char]:
#         worst_char = k

# print('worst_char--->', worst_char)


##########################################

# Create a dictionary named letter_counts that contains each letter and the number of times it occurs in string1. Challenge: Letters should not be counted separately as upper-case and lower-case. Intead, all of them should be counted as lower-case.

# string1 = "There is a tide in the affairs of men, Which taken at the flood, leads on to fortune. Omitted, all the voyage of their life is bound in shallows and in miseries. On such a full sea are we now afloat. And we must take the current when it serves, or lose our ventures."

# string2 = string1.lower()

# letter_counts = {}

# for c in string2:
#     if c not in letter_counts:
#         letter_counts[c] = 0
#     letter_counts[c] = letter_counts[c] + 1

# print(letter_counts)

##########################################

# Create a dictionary called low_d that keeps track of all the characters in the string p and notes how many times each character was seen. Make sure that there are no repeats of characters as keys, such that “T” and “t” are both seen as a “t” for example.

# p = "Summer is a great time to go outside. You have to be careful of the sun though because of the heat."
# p1 = p.lower()

# low_d = {}
# print('low_d', low_d)
# for c in p1:
#     if c not in low_d:
#         low_d[c] = 0
#     low_d[c] = low_d[c] + 1

# print('low_d', low_d)



