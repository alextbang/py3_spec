
# import turtle            # set up alex
# wn = turtle.Screen()
# alex = turtle.Turtle()

# for loop #1

# for i in [0, 1, 2, 3]:      # repeat four times
#     alex.forward(50)
#     alex.left(90)


# for loop #2

# for e in range(4):
#     alex.forward(50)
#     alex.left(90)

# wn.exitonclick()

#################################


# print("range(5): ")
# for i in range(5):
#     print(i)

# print("range(0,5): ")
# for i in range(0, 5):
#     print(i)

# # Notice the casting of `range` to the `list`
# print(list(range(5)))
# print(list(range(0,5)))

# # Note: `range` function is already casted as `list` in the textbook
# print(range(5))


#####################################

### create a list of integers from 0 through 52 and assign that list to the variable numbers
# cast range in a list to use the method outside of iterator (for loop)

# numbers = list(range(0,53))
# print(numbers)
    

#####################################

# Create a list of numbers 0 through 40 and assign this list to the variable numbers. 
# Then, accumulate the total of the list’s values and assign that sum to the variable sum1.

# numbers = range(41)

# sum1 = 0
# for e in numbers:
#     sum1 = sum1 + e
# print(sum1)

#######################################

'''addition_str is a string with a list of numbers separated by the + sign. Write code that uses the accumulation pattern to take the sum of all of the numbers and assigns it to sum_val (an integer). (You should use the .split("+") function to split by "+" and int() to cast to an integer).
addition_str = "2+5+10+20" '''

# new_str = addition_str.split("+")

# sum_val = 0
# for e in new_str:
#     sum_val = sum_val + int(e)
#     print(e)
# print(sum_val)


########################################
'''week_temps_f is a string with a list of fahrenheit temperatures separated by the , sign. Write code that uses the accumulation pattern to compute the average (sum divided by number of items) and assigns it to avg_temp. Do not hard code your answer (i.e., make your code compute both the sum or the number of items in week_temps_f) (You should use the .split(",") function to split by "," and float() to cast to a float).'''

# week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"
# temps = week_temps_f.split(",")

# avg_temp = 0
# for e in temps:
#     avg_temp = avg_temp + float(e)
# avg_temp = avg_temp / len(temps)
 

##########################################

'''Write code to create a list of word lengths for the words in original_str using the accumulation pattern and assign the answer to a variable num_words_list. (You should use the len function).'''

# original_str = "The quick brown rhino jumped over the extremely lazy fox"
# string1 = original_str.split(" ")

# num_words_list = []

# for e in string1:
#     num_words_list.append(len(e))
# print(num_words_list)


############################################

'''Create an empty string and assign it to the variable lett. Then using range, write code such that when your code is run, lett has 7 b’s ("bbbbbbb").'''

# lett = ""
# for e in range(7):
#     lett = lett + "b"
# print(lett)


############################################
