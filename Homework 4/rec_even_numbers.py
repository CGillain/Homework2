### Introduction to Python ###
######## Homework 4 ##########

# In the one with recursive even numbers, change it to calculate n! recursively.
# Remember that 4! = 1x2x3x4 and n! = (n-1)! x n and that 0! = 1


num = input("Please enter a non negative number you want the factorial from:")
def recur_factorial(n):
    if n == 1 or n == 0:
       return n
    elif n < 0:
       print("Error: You cannot do the factorial of this number")

    else:
       return n*recur_factorial(n-1)

print (recur_factorial(int(num)))



