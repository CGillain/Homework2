### Introduction to Python ###
######## Homework 4 ##########


# In the one with the doubled letters: check again if all the letters are tripled. Ex: aaabbbcccdddEEE

string = input("Give me the text please: ")

if (string[::3] == string[1::3]) and (string[1::3] == string[2::3]):
    print("They are all tripled ")
else:
    print("They are not all tripled")


