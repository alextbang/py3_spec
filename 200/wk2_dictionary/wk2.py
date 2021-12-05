# update 

# inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
# inventory['bananas'] = inventory['bananas'] + 200
# numItems = len(inventory)
# print(inventory['bananas'])

###############################################

### Count the number of times a letter shows up in the file 'scarlet.txt'.
# 

# f = open('scarlet.txt', 'r')
# txt = f.read()

# # now 'txt' is one long string containing all the characters
# letter_counts = {} # start with an empty dictionary

# for c in txt:
#     if c not in letter_counts:
#         # we have not seen this character before, so initialize a counter for it
#         letter_counts[c] = 0

#     #whether we've seen it before or not, increment its counter
#     letter_counts[c] = letter_counts[c] + 1

# for c in letter_counts.keys():
#     print(c + ": " + str(letter_counts[c]) + " occurrences")

###############################################

# Split the string into a list of words, then craete a dicitionary that contains each word and the number of times it occurs. Save this dictionary to the variable name word_counts.

# sentence = "The dog chased the rabbit into the forest but the rabbit was too quick."
# words = sentence.split()
# # print('words-->', words)

# word_counts = {}

# for w in words:
#     if w not in word_counts:
#         # we have not seen this word, so initialize a counter for it
#         word_counts[w] = 0  

#     # increment counter for the current word
#     word_counts[w] += 1  

# print('wordCcounts--->', word_counts)

###############################################

# Create a dictionary called 'char_d' from the string 'stri', so that the key is a character and the value is how many times it coours.

# stri = "what can I do" 
# char_d = {}

# for c in stri:
#     if c not in char_d:
#         char_d[c] = 0
    
#     char_d[c] += 1

# print('char_d --->', char_d)

###############################################

# Each occurrence of the letter ‘e’ earns one point, but ‘q’ earns 10. We have a second dictionary, stored in the variable letter_values. Now, to compute the total score, we start an accumulator at 0 and go through each of the letters in the counts dictionary. For each of those letters that has a letter value (no points for spaces, punctuation, capital letters, etc.), we add to the total score.

# f = open('sample.txt', 'r')
# txt = f.read()
# # now txt is one long string containing all the characters
# x = {} # start with an empty dictionary
# for c in txt:
#     if c not in x:
#         # we have not seen this character before, so initialize a counter for it
#         x[c] = 0

#     #whether we've seen it before or not, increment its counter
#     x[c] = x[c] + 1

# letter_values = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f':4, 'g': 2, 'h':4, 'i':1, 'j':8, 'k':5, 'l':1, 'm':3, 'n':1, 'o':1, 'p':3, 'q':10, 'r':1, 's':1, 't':1, 'u':1, 'v':8, 'w':4, 'x':8, 'y':4, 'z':10}

# tot = 0
# for y in x:
#     if y in letter_values:
#         tot = tot + letter_values[y] * x[y]

# print('total-->', tot)

#################################################

#  The dictionary travel contains the number of countries within each continent that Jackie has traveled to. Find the total number of countries that Jackie has been to, and save this number to the variable name total.
 
travel = {"North America": 2, "Europe": 8, "South America": 3, "Asia": 4, "Africa":1, "Antarctica": 0, "Australia": 1}

total = 0
#iterate dictionary and get the sum of all values

for c in travel:
    total = total + travel[c]
    print(travel[c])

print("total", total)

#################################################

# # schedule is a dictionary where a class name is a key and its value is how many credits it was worth. Accumulate the total number of credits that have been earned so far and assign that to the variable total_credits.

# schedule = {"UARTS 150": 3, "SPANISH 103": 4, "ENGLISH 125": 4, "SI 110": 4, "ENS 356": 2, "WOMENSTD 240": 4, "SI 106": 4, "BIO 118": 3, "SPANISH 231": 4, "PSYCH 111": 4, "LING 111": 3, "SPANISH 232": 4, "STATS 250": 4, "SI 206": 4, "COGSCI 200": 4, "AMCULT 202": 4, "ANTHRO 101": 4}

# total_credits = 0

# for c in schedule:
#     total_credits += schedule[c]

# print('total credits-->', total_credits)


##################################################

# Create a dictionary called d that keeps track of all the characters in the string placement and notes how many times each character was seen. Then, find the key with the lowest value in this dictionary and assign that key to min_value.

# placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."
# d = {}

# for c in placement:
#     if c not in d:
#         d[c] = 0
#     d[c] += 1
# print('d-->', d)

# ks = d.keys()
# # Have to turn dictionary keys into a real list before using [] to select an item
# min_value = list(ks)[0]
# for k in ks:
#     if d[k] < d[min_value]:
#         min_value = k

# print("key " + min_value + " has the min value of " + str(d[min_value]))


#################################################

 ##Create a dictionary called lett_d that keeps track of all of the characters in the string product and notes how many times each character was seen. Then, find the key with the highest value in this dictionary and assign that key to max_value.

# product = "iphone and android phones"
# lett_d = {}

# for c in product:
#     if c not in lett_d:
#         lett_d[c] = 0
#     lett_d[c] += 1
# print('lett_d--->',lett_d)

# ks = lett_d.keys()
# print('ks--->',ks)

# max_value = list(ks)[0]

# for k in ks:
#     if lett_d[k] > lett_d[max_value]:
#         max_value = k

# print('max_value--->', max_value)

##################################################


