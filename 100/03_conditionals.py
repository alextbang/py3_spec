# nested conditionals

# x = 10
# y = 10

# if x < y:
#     print("x is less than y")
# else:
#     if x > y:
#         print("x is greater than y")
#     else:
#         print("x and y must be equal")

####################################


# x = 10
# y = 10

# if x < y:
#     print("x is less than y")
# elif x > y:
#     print("x is greater than y")
# else:
#     print("x and y must be equal")

#######################################

# nested if-else statement

x = -10

# if x < 0:
#     print("The negative number ",  x, " is not valid here.")
# else:
#     if x > 0:
#         print(x, " is a positive number")
#     else:
#         print(x, " is 0")

###############################


# if x < 0:
#     print("The negative number ",  x, " is not valid here.")
# elif (x > 0):
#     print(x, " is a positive number")
# else:
#     print(x, " is 0")


###############################


# if x < 0:
#     print("The negative number ",  x, " is not valid here.")
# if (x > 0):
#     print(x, " is a positive number")
# else:
#     print(x, " is 0")
       

#################################

str1 = "Today you are you! That is truer than true! There is no one alive who is you-er than you!"

if "false" in str1:
    output = "False. You aren't you?"
elif "true" in str1:
    output = "True! You are you!"
else:
    output = "Neither true nor false!"

print(output)

#################################

# ```Create an empty list called resps. Using the list percent_rain, for each percent, if it is above 90, add the string ‘Bring an umbrella.’ to resps, otherwise if it is above 80, add the string ‘Good for the flowers?’ to resps, otherwise if it is above 50, add the string ‘Watch out for clouds!’ to resps, otherwise, add the string ‘Nice day!’ to resps.```


# percent_rain = [94.3, 45, 100, 78, 16, 5.3, 79, 86]
# resps = []

# for e in percent_rain:
#     if e > 90:
#         resps.append("Bring an umbrella.")
#     elif e > 80:
#         resps.append("Good for the flowers?")
#     elif e > 50:
#         resps.append("Watch out for clouds!")
#     else:
#         resps.append("Nice day!")

###################################


# ```rainfall_mi is a string that contains the average number of inches of rainfall in Michigan for every month (in inches) with every month separated by a comma. Write code to compute the number of months that have more than 3 inches of rainfall. Store the result in the variable num_rainy_months. In other words, count the number of items with values > 3.0.```

# rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"
# rainfall_list = []
# num_rainy_months = 0

# rainfall_list = rainfall_mi.split(", ")

# for rain in rainfall_list:
#     if float(rain) > 3.0:
#         num_rainy_months += 1

# print(num_rainy_months)

##########################################

# The variable sentence stores a string. Write code to determine how many words in sentence start and end with the same letter, including one-letter words. Store the result in the variable same_letter_count.

# sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"

# # Write your code here.
# words = []
# same_letter_count = 0

# words = sentence.split(" ")

# for word in words:
#     if word[0] == word[-1]:
#         same_letter_count += 1


##############################################



