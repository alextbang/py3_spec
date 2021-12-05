#1

# The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary. Find the total number of characters in the file and save to the variable num.

# file = open("travel_plans2.txt", "r")
# data = file.read()
# num = len(data)
# print(num)
#print(data)

############################################

#2

# We have provided a file called emotion_words.txt that contains lines of words that describe emotions. Find the total number of words in the file and assign this value to the variable num_words.

file = open("emotion_words.txt", "r")
lines = file.readlines()
print("lines--> :) ", lines) 

num_words = 0
for line in lines:
    num_words += len(line.split())
    print("line split-->", line.split())
print("num_words:", num_words)

############################################

# Assign to the variable num_lines the number of lines in the file school_prompt.txt.

# file = open("school_prompt.txt", "r")
# num_lines = 0

# for line in file:
#     num_lines += 1

############################################

# Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars.

# file = open("school_prompt.txt", "r")
# beginning_chars = file.read(30)

############################################

# Using the file school_prompt.txt, assign the third word of every line to a list called three.

# file = open("school_prompt2.txt", "r")
# lines = file.readlines()
# print("lines-->", lines)

# three = []

# for line in lines:
#     line = line.split()
#     print("line--->", line)
#     three.append(line[2])
# #print("words -->", words)
# print("new line--->", three)

############################################

# Create a list called emotions that contains the first word of every line in emotion_words.txt.

# file = open("emotion_words.txt", "r")
# lines = file.readlines()
# emotions = []

# for line in lines:
#     line = line.split()
#     emotions.append(line[0])

############################################

# Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars.

# file = open('travel_plans.txt', 'r')
# first_chars = file.read(33)

############################################

##Challenge: Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words.

# file = open("school_prompt2.txt", "r")
# lines = file.readlines()
# print("lines:", lines)

# p_words = []

# for line in lines:
#     line = line.split()
#     print("word--->", line)
#     for word in line:
#         if 'p' in word:
#             p_words.append(word)

# print("p_words--->", p_words)
