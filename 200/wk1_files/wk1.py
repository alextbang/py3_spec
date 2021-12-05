###########################
#### Working with files ###
###########################

# # Using the file school_prompt2.txt, find the number of characters in the file and assign that value to the variable num_char.

# # open file in read mode and create a file "object" 
# fileref = open("./school_prompt2.txt", "r")
# num_char = 0

# # read the entire content of file as a single string
# data = fileref.read()

# # get the length of the data
# num_char = len(data)

# print("total characters:", num_char)


###############################################

# # Using the file travel_plans2.txt, find the number of lines in the file.

# # open file in read mode and create a file "object" 
# file = open("./travel_plans2.txt", "r")
# num_lines = 0

# # read the file and return all lines in the files as list where each line is an item in the list
# data = file.readlines()

# # get the length of the data
# num_lines = len(data)

# print("total lines:", num_lines)

###############################################

# Create a string called first_forty that is comprised of the first 40 characters of emotion_words2.txt.

# file = open("./emotion_words2.txt", "r")
# first_forty = file.read(40)
# print(first_forty)


###############################################

# count number of lines in a file

# emotion_words = open("./emotion_words.txt", "r")
# num_lines = 0

# # parse directly without reading the entire file in as an object first
# for aline in emotion_words:
#     num_lines += 1

# print("Total number of lines:", num_lines)
# emotion_words.close()

###############################################

# filename = "squared_numbers.txt"
# outfile = open(filename, "w")

# for number in range(1, 13):
#     square = number * number
#     outfile.write(str(square) + "\n")

# outfile.close()

# infile = open(filename, "r")
# print(infile.read()[:10])
# infile.close()

###############################################

# # use 'with' to handle file
#
# # code 1 here is the same as code 2 
# with open('emotion_words.txt', 'r') as md:
#     for line in md:
#         print(line)
# # continue on with other code
# # file automatically closed

##
# code 2
# md = open('emotion_words.txt', 'r')
# for line in md:
#     print(line)
# md.close()
# continue with other code

###################################################

##################################################
#### Recipe for Reading and Processing a File ####
##################################################


# # Here’s a foolproof recipe for processing the contents of a text file. If you’ve fully digested the previous sections, you’ll understand that there are other options as well. Some of those options are preferable for some situations, and some are preferred by python programmers for efficiency reasons. In this course, though, you can always succeed by following this recipe.

# #1. Open the file using with and open.

# #2. Use .readlines() to get a list of the lines of text in the file.

# #3. Use a for loop to iterate through the strings in the list, each being one line from the file. On each iteration, process that line of text

# #4. When you are done extracting data from the file, continue writing your code outside of the indentation. Using with will automatically close the file once the program exits the with block.

# fname = "yourfile.txt"
# with open(fname, 'r') as fileref:         # step 1
#     lines = fileref.readlines()           # step 2
#     for lin in lines:                     # step 3
#         #some code that references the variable lin
# #some other code not relying on fileref   # step 4

# However, this will not be good to use when you are working with large data. Imagine working with a datafile that has 1000 rows of data. It would take a long time to read in all the data and then if you had to iterate over it, even more time would be necessary. This would be a case where programmers prefer another option for efficiency reasons.

# This option involves iterating over the file itself while still iterating over each line in the file:

# fname = "yourfile.txt"
# with open(fname, 'r') as fileref:         # step 1
#     for lin in fileref:                   # step 2
#         ## some code that reference the variable lin
# #some other code not relying on fileref   # step 3


###################################################

