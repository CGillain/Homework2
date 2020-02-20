### Introduction to Python ###
######## Homework 4 ##########

# In the one with max 4 numbers: change it to read the number of numbers first and then read all the numbers and print the max.
# Note from Celine: I am not sure i understand what you mean with this.... just printed the unsorted list and then sorted it.


numbers=[]
count=0

while True:
    if count >= 4:
        break
    number= input("Enter a number: ")
    try:
        number= int(number)
    except:
        print("That was not a number")
        continue
    #We have a proper number
    numbers.append(number)
    count += 1


print(numbers)

numbers.sort()

print("This is the same list sorted from the smallest to the largest number: ", numbers)

print("The maximum is {} ".format(numbers[3]))
