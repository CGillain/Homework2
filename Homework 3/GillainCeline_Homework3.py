############ INTRODUCTION TO PYTHON #################
################## Homework 3 #######################


### Guidelines:

# Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
# For example, if s = 'azcbobobegghakl', then your program should print: Longest substring in alphabetical order is: beggh

# In the case of ties, print the first substring. For example, if s = 'abcbcd',
# then your program should print:Longest substring in alphabetical order is: abc

# Input
s = input(" Please enter any string of letters: ")

# Defining two strings, the initial one and the longest substring in
# alphabetical order

string = s[0]
substring = s[0]

# For loop
for i in s[1:]:
    if i >= string[-1]:
        string += i
        if len(string) > len(substring):
            substring = string
    else:
        string = i
print ("Longest substring in alphabetical order is:", substring)