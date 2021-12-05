

##################################################

# Final assessment #1
#
# '''Below are a set of scores that students have received in the past semester. Write code to determine how many are 90 or above and assign that result to the value a_scores.'''


# scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"
# scores_int = scores.split()
# print('scores_int', scores_int)
# a_scores = 0

# for i in scores_int:
#     if int(i) >= 90:
#         a_scores += 1

# print('A scores:', a_scores)


#####################################################

# # Final assessment 2

# '''Write code that uses the string stored in "org" and creates an acronym which is assigned to the variable "acro". Only the first letter of each word should be used, each letter in the acronym should be a capital letter, and there should be nothing to separate the letters of the acronym. Words that should not be included in the acronym are stored in the list stopwords.'''

# stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
# org = "The organization for health, safety, and education"
# acro = ""

# # # start code below

# # remove commas from org string
# org = org.replace(',', '')
# print("org:", org) # THE ORGANIZATION FOR HEALTH SAFETY AND EDUCATION

# acro_words = org.split()
# print("acro_words 1:", acro_words)

# # remove forbidden words
# for w in acro_words:
#     if w in stopwords:
#         acro_words.remove(w)

# print('acro_words with no bad words:', acro_words)
# # ['organization', 'health,', 'safety,', 'education']

# # get first letter of each word
# acro_list = []
# for i in range(len(acro_words)):
#     acro_list.append(acro_words[i][0]) 

# print(acro_list) #['o', 'h', 's', 'e']

# # convert list to a string and change to upper case
# acro = ''.join(acro_list)
# acro = acro.upper()
# print("acro:", acro)


#####################################################

# Final assessment 3
#
# ```Write code that uses the string stored in sent and creates an acronym which is assigned to the variable acro. The first two letters of each word should be used, each letter in the acronym should be a capital letter, and each element of the acronym should be separated by a “. ” (dot and space). Words that should not be included in the acronym are stored in the list stopwords. ```

# stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
# sent = "The water earth and air are vital"
# acro = ""

# # create a list of words from string
# sent_words = sent.split()
# print("sent words -->", sent_words)  # ['The', 'water', 'earth', 'and', 'air', 'are', 'vital']

# # remove stopwords from sent string
# for w in sent_words:
#     if w in stopwords:
#         sent_words.remove(w)

# print("filtered sent words -->", sent_words)  #['water', 'earth', 'air', 'are', 'vital']
   
# #grab first two letters from each item in the list
# acro_list = []
# for e in sent_words:
#     acro_list.append(e[0:2])

# print("acro list -->", acro_list)

# acro = ". ".join(acro_list)
# acro = acro.upper()
# print("acro -->", acro)


###########################################################

# Final assessment 4
#
# Write code that checks if p_phrase is a palindrome by reversing it and then checking if the reversed version is equal to the original. 
# 
#
# p_phrase = "was it a car or a cat I saw"
# r_phrase = ""
#
# reverse the string
#
# for i in p_phrase:
#     r_phrase = i + r_phrase

###########################################################

# # Final assessment 5
# # Print out each item in the list with the same formatting, using the .format method (not string concatenation).

# #
# inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]
# i_list = []

# # break each inventory list item to it's own smaller list containing three items
# for i in inventory:
#     i_list.append(i.split(','))
# print("i list -->", i_list)
# # [['shoes', ' 12', ' 29.99'], ['shirts', ' 20', ' 9.99'], ['sweatpants', ' 25', ' 15.00'], ['scarves', ' 13', ' 7.75']]

# for i in i_list:
#     print('The store has{} {}, each for{} USD.'.format(i[1], i[0], i[2]))

